from nixdiskmanager.constants import rootdir
from nixdiskmanager.dialogs.manage_disk import NixDiskManagerManageDiskDialog
from nixdiskmanager.utils.size_parser import parse_size

from gi.repository import Gtk

@Gtk.Template(resource_path = rootdir + '/disk.ui')
class NixDiskManagerDisk(Gtk.Box):
    __gtype_name__ = "NixDiskManagerDisk"
    label = Gtk.Template.Child('label')
    manage_btn = Gtk.Template.Child('manage-btn')

    def __init__(self, disk, parent, window, **kwargs):
        super().__init__(**kwargs)

        self.disk = disk
        self.parent = parent

        self.label.set_label(f'{self.disk.path} ({parse_size(self.disk.size)})')

        self.window = window

    @Gtk.Template.Callback()
    def show_disk_dialog(self, window):
        dialog = NixDiskManagerManageDiskDialog(self.disk, window, self.parent)
        dialog.present(window)

    def prevent_changes(self):
        self.manage_btn.set_sensitive(False)

    def allow_changes(self):
        self.manage_btn.set_sensitive(True)