from nixdiskmanager.dialogs.manage_disk_mount_row import NixDiskManagerManageDiskMountRow
from nixdiskmanager.dialogs.manage_disk_add_mount_row import NixDiskManagerManageDiskAddMountRow
from nixdiskmanager.utils.size_parser import parse_size
from nixdiskmanager.constants import rootdir

import os
from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = rootdir + '/manage_disk_mount_expander.ui')
class NixDiskManagerManageDiskDialogMountExpander(Adw.ExpanderRow):
    __gtype_name__ = "NixDiskManagerManageDiskDialogMountExpander"
    add_button = Gtk.Template.Child('add-button')

    def __init__(self, partition, app, **kwargs):
        super().__init__(**kwargs)

        self.app = app
        self.set_title((partition.label + ' - ' if partition.label != None else '') + partition.path + f' ({partition.type}, {parse_size(partition.size)})')
        self.partition = partition

        for mount_point in partition.mount_points:
            self.add_row(NixDiskManagerManageDiskMountRow(mount_point, self))

    def add_mount_point(self, mount_point, apply_target, create_dir):
        dir_created = True

        if create_dir:
            code = os.system(f'pkexec nix-disk-manager-cli mkdir {mount_point}')

            if code != 0:
                dir_created = False

        if not dir_created:
            return
        
        self.remove(apply_target)

        self.add_row(NixDiskManagerManageDiskMountRow(mount_point, self))
        self.add_button.set_sensitive(True)
        self.partition.mount_points.append(mount_point)
        self.app.change_detected()

    def delete_mount_point(self, mount_point, target):
        self.remove(target)
        self.partition.mount_points.remove(mount_point)
        self.app.change_detected()

    @Gtk.Template.Callback()
    def add_expand(self, button):
        self.add_button.set_sensitive(False)
        self.set_expanded(True)
        row = NixDiskManagerManageDiskAddMountRow(self)
        self.add_row(row)
        row.grab_focus_without_selecting()
