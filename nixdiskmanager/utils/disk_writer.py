from nixdiskmanager.utils.disk import Disk

def get_nix_disks_config(nix_config, disks: list[Disk]):
    config = nix_config
    
    file_sys_config_pos = config.find('fileSystems."')
    while file_sys_config_pos != -1:
        close_expr_pos = config.find('};', file_sys_config_pos)

        config = config[:file_sys_config_pos] + config[close_expr_pos + 3:]
        file_sys_config_pos = config.find('fileSystems."')

    config = config[:-2]

    for disk in disks:
        for partition in disk.partitions:
            if len(partition.mount_points) == 0:
                continue

            for mount_point in partition.mount_points:
                fs_options = '[ "defaults" "nofail" "x-gvfs-show" ]'

                if partition.type == 'btrfs':
                    fs_options = '[ "defaults" "nofail" "x-gvfs-show" "compress=zstd" ]'
                elif partition.type == 'ntfs' or partition.type == 'ntfs3':
                    fs_options = '[ "nofail" "x-gvfs-show" "uid=1000" "gid=1000" "rw" "user" "exec" "umask=000" "defaults" "0 0" ]'

                if mount_point == '/' or mount_point == '/boot':
                    fs_options = fs_options.replace(' "x-gvfs-show"', '')
                
                config += f'  fileSystems."{mount_point}" = ' + '{\n'
                config += f'    device = "{partition.uuid_path}";\n'
                config += f'    fsType = "{partition.type}";\n'
                config += f'    options = {fs_options};\n'
                config += '  };\n\n'

    config += '}'
    return config
