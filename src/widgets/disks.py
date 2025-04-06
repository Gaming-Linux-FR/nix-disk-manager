from enum import Enum

from utils import proc_parser
from widgets.disk import NixDiskManagerDisk

import pathlib
import gi

BASE_DIR = pathlib.Path(__file__).resolve().parent

gi.require_version('Adw', '1')
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Adw, Gio

@Gtk.Template(filename = BASE_DIR.as_posix() + '/../../data/ui/widgets/disks.ui')
class NixDiskManagerDisks(Gtk.Box):
    __gtype_name__ = "NixDiskManagerDisks"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        disks = proc_parser.parse_proc_disks()

        for disk in disks:
            disk_widget = NixDiskManagerDisk(disk)
            self.append(disk_widget)