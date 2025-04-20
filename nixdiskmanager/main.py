import sys, subprocess
from gi.repository import GLib, Adw, Gio

from concurrent.futures import ThreadPoolExecutor as Pool

from nixdiskmanager.views.main_window import NixDiskManagerMainWindow
from nixdiskmanager.widgets.disks import NixDiskManagerDisks
from nixdiskmanager.utils.disk_parser import get_disks
from nixdiskmanager.utils.disk_writer import get_nix_disks_config

class NixDiskManagerApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="org.glfos.nixdiskmanager")
        GLib.set_application_name('Nix Disk Manager')
        GLib.set_prgname('nix-disk-manager')

        self.add_action(Gio.SimpleAction.new('quit'))

        self.nix_rebuild_cmd = 'nixos-rebuild switch'
        self.hardware_config_file = '/etc/nixos/hardware-configuration.nix'
        self.must_save = False

        with open(self.hardware_config_file, 'r') as f:
            self.hardware_config = f.read()
        
        self.disks = get_disks(self.hardware_config)

    def do_activate(self):
        self.window = NixDiskManagerMainWindow(application=self)
        self.disk_manager = NixDiskManagerDisks(self.window, self)
        self.window.get_content().append(self.disk_manager)
        self.window.present()

    def rebuild_finished(self, future):
        res = future.result()
        self.window.rebuild_banner.set_revealed(False)

        if res == 0:
            self.must_save = False
            self.disk_manager.allow_changes()
        else:
            self.window.rebuild_error_banner.set_revealed(True)

    def save_config(self):
        f = open(self.hardware_config_file, 'w')
        f.write(get_nix_disks_config(self.hardware_config, self.disks))
        f.close()

        self.window.rebuild_error_banner.set_revealed(False)
        self.window.rebuild_banner.set_revealed(True)
        self.disk_manager.prevent_changes()

        pool = Pool(max_workers=1)
        f = pool.submit(subprocess.call, self.nix_rebuild_cmd, shell=True)
        f.add_done_callback(self.rebuild_finished)

def main():
    app = NixDiskManagerApp()
    exit_status = app.run(sys.argv)
    return exit_status
