from nixdiskmanager.dialogs.manage_disk_mount_expander import NixDiskManagerManageDiskDialogMountExpander
from nixdiskmanager.constants import rootdir

from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = rootdir + '/manage_disk.ui')
class NixDiskManagerManageDiskDialog(Adw.Dialog):
    __gtype_name__ = "NixDiskManagerManageDiskDialog"
    mount_points = Gtk.Template.Child('mount-points')

    def __init__(self, disk, window, app, **kwargs):
        super().__init__(**kwargs)

        self.set_title(disk.path)
        
        for partition in disk.partitions:
            self.mount_points.add(NixDiskManagerManageDiskDialogMountExpander(partition, app))

        if len(disk.partitions) == 0:
            label = Gtk.Label()
            label.set_text(_('No mount points were detected'))
            self.mount_points.add(label)

