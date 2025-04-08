from nixdiskmanager.constants import rootdir
from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = rootdir + '/manage_disk_mount_row.ui')
class NixDiskManagerManageDiskMountRow(Adw.ActionRow):
    __gtype_name__ = "NixDiskManagerManageDiskMountRow"

    delete_btn = Gtk.Template.Child('delete-btn')

    def __init__(self, mount_point, parent, **kwargs):
        super().__init__(**kwargs)

        self.set_title(mount_point)

        self.parent = parent
        self.mount_point = mount_point

        if mount_point == '/boot' or mount_point == '/':
            self.delete_btn.set_sensitive(False)

    @Gtk.Template.Callback()
    def on_delete(self, target):
        self.parent.delete_mount_point(self.mount_point, self)