from nixdiskmanager.constants import rootdir
from nixdiskmanager.dialogs.save_dialog import NixDiskManagerManageSaveDialog
from nixdiskmanager.dialogs.welcome_dialog import NixDiskManagerWelcomeDialog
from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = rootdir +'/window.ui')
class NixDiskManagerMainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "NixDiskManagerMainWindow"

    rebuild_banner = Gtk.Template.Child('rebuild-banner')
    rebuild_error_banner = Gtk.Template.Child('rebuild-error-banner')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = Adw.Application.get_default()
        self.set_icon_name('nix-disk-manager')

        welcome_dialog = NixDiskManagerWelcomeDialog()

        welcome_dialog.present(self)

    @Gtk.Template.Callback()
    def on_close(self, target):
        if self.app.must_save:
            NixDiskManagerManageSaveDialog(self).present(self)
            return True
