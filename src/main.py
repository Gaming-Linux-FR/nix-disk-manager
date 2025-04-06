import sys

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import GLib, Adw

from views.main_window import NixDiskManagerMainWindow
from widgets.disks import NixDiskManagerDisks

class NixDiskManagerApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="org.glfos.nixdiskmanager")
        GLib.set_application_name('Nix Disk Manager')

    def do_activate(self):
        window = NixDiskManagerMainWindow(application=self)

        window.get_content().append(NixDiskManagerDisks())
        window.present()


app = NixDiskManagerApp()
exit_status = app.run(sys.argv)
sys.exit(exit_status)