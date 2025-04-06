from enum import Enum

import pathlib
import gi

BASE_DIR = pathlib.Path(__file__).resolve().parent

gi.require_version('Adw', '1')
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Adw, Gio

@Gtk.Template(filename = BASE_DIR.as_posix() + '/../../data/ui/widgets/disk.ui')
class NixDiskManagerDisk(Gtk.Box):
    __gtype_name__ = "NixDiskManagerDisk"
    label = Gtk.Template.Child('label')

    def __init__(self, disk_path, **kwargs):
        super().__init__(**kwargs)

        self.disk_path = disk_path
        self.label.set_label(self.disk_path)