from nixdiskmanager.constants import rootdir
from nixdiskmanager.widgets.disk import NixDiskManagerDisk

from gi.repository import Gtk

@Gtk.Template(resource_path = rootdir + '/disks.ui')
class NixDiskManagerDisks(Gtk.Box):
    __gtype_name__ = "NixDiskManagerDisks"
    container = Gtk.Template.Child('container')
    save_btn = Gtk.Template.Child('save-btn')

    def __init__(self, window, app, **kwargs):
        super().__init__(**kwargs)

        self.app = app
        self.disks_widgets = []

        for disk in self.app.disks:
            disk_widget = NixDiskManagerDisk(disk, self, window)
            self.disks_widgets.append(disk_widget)
            self.container.append(disk_widget)

        self.prevent_save()

    def change_detected(self):
        self.save_btn.set_sensitive(True)
        self.app.must_save = True

    def prevent_save(self):
        self.save_btn.set_sensitive(False)

    def prevent_changes(self):
        self.prevent_save()
        for disk in self.disks_widgets:
            disk.prevent_changes()

    def allow_changes(self):
        for disk in self.disks_widgets:
            disk.allow_changes()

    @Gtk.Template.Callback()
    def on_save(self, btn):
        self.app.save_config()