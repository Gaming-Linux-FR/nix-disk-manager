from enum import Enum

import pathlib
import gi

BASE_DIR = pathlib.Path(__file__).resolve().parent

gi.require_version('Adw', '1')
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Adw, Gio

@Gtk.Template(filename = BASE_DIR.as_posix() + '/../../data/ui/window.ui')
class NixDiskManagerMainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "NixDiskManagerMainWindow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = Adw.Application.get_default()