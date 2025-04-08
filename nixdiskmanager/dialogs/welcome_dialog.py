import sys

from nixdiskmanager.constants import rootdir, pkgdatadir
from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = rootdir + '/welcome_dialog.ui')
class NixDiskManagerWelcomeDialog(Adw.Dialog):
    __gtype_name__ = "NixDiskManagerWelcomeDialog"

    logo = Gtk.Template.Child('logo')
    start_btn = Gtk.Template.Child('start-btn')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logo.set_filename(pkgdatadir + '/logo.png')

    @Gtk.Template.Callback()
    def start(self, target):
        self.close()
