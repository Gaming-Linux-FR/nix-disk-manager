from nixdiskmanager.constants import rootdir
import os

from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = rootdir + '/manage_disk_add_mount_row.ui')
class NixDiskManagerManageDiskAddMountRow(Adw.EntryRow):
    __gtype_name__ = "NixDiskManagerManageDiskAddMountRow"

    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)

        self.parent = parent
        self.mount_prefix = '/media/'
        self.set_text(self.mount_prefix)
        self.set_position(-1)

    @Gtk.Template.Callback()
    def on_apply(self, target):
        text = target.get_text()
        
        if text == '' or text == '/media' or text == '/media/':
            return
        if not text.startswith('/'):
            mount_point = '/media/' + text
        else:
            mount_point = text

        if os.path.exists(mount_point) and len(os.listdir(mount_point)) > 0:
            return

        self.parent.add_mount_point(mount_point, target)