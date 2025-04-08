import sys

from nixdiskmanager.constants import rootdir
from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = rootdir + '/save_dialog.ui')
class NixDiskManagerManageSaveDialog(Adw.AlertDialog):
    __gtype_name__ = "NixDiskManagerManageSaveDialog"

    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)
        self.window = window

    @Gtk.Template.Callback()
    def response(self, target, response):
        if response == 'exit':
            sys.exit()
