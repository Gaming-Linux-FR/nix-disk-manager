from nixdiskmanager.constants import rootdir
from nixdiskmanager.dialogs.manage_disk import NixDiskManagerManageDiskDialog

from gi.repository import Gtk

@Gtk.Template(resource_path = rootdir + '/disk.ui')
class NixDiskManagerDisk(Gtk.Box):
    __gtype_name__ = "NixDiskManagerDisk"
    label = Gtk.Template.Child('label')

    def __init__(self, disk, parent, window, **kwargs):
        super().__init__(**kwargs)

        self.disk = disk
        self.parent = parent
        self.label.set_label(self.disk.path)
        self.window = window

    @Gtk.Template.Callback()
    def show_disk_dialog(self, window):
        dialog = NixDiskManagerManageDiskDialog(self.disk, window, self.parent)
        dialog.present(window)
