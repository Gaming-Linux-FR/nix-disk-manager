from nixdiskmanager.utils.partition import Partition
from nixdiskmanager.utils.disk import Disk

import os, re, subprocess

def parse_nix_filesystems(nix_config) -> dict[str, Partition]:
    # Find all filesystems configurations
    mounts_matches = [x for x in re.finditer('fileSystems\\."(.+)"', nix_config)]
    
    partitions_dict = {}

    for mount_match in mounts_matches:
        nix_group = nix_config[mount_match.start():nix_config.find('}', mount_match.start())+1]
        mount_point = mount_match.group(1)
        partition_uuid_path = re.search('device = "(.+)"', nix_group).group(1)
        partition_path = os.path.abspath('/'.join(partition_uuid_path.split('/')[:-1]) + '/' + os.readlink(partition_uuid_path))

        if partition_path not in partitions_dict:
            partitions_dict[partition_path] = Partition(partition_path, partition_uuid_path, [mount_point], None, None)
        else:
            partitions_dict[partition_path].mount_points.append(mount_point)

    return partitions_dict

def get_disks(nix_config = None) -> list[Disk]:
    if nix_config == None:
        partitions = {}
    else:
        partitions = parse_nix_filesystems(nix_config)

    content = []

    with open('/proc/partitions', 'r') as proc_file:
        content = proc_file.readlines()

    content = content[2:]
    
    disks = []

    for disk_line in content:
        disk = '/dev/' + disk_line.split(' ')[-1].strip()

        # Exclude zram and CD/DVD
        if disk.startswith('/dev/zram') or disk.startswith('/dev/sr'):
            continue

        disk_size = int(subprocess.getoutput(f'lsblk -b --output SIZE -n -d {disk}'))
        
        if len(disks) > 0 and disk.startswith(disks[-1].path):
            blkid = subprocess.getoutput(f'blkid {disk}')

            partition_type_match = re.search('TYPE="([^"]+)"', blkid)
            partition_type = None if partition_type_match == None else partition_type_match.group(1)

            partition_label_match = re.search('LABEL="([^"]+)"', blkid)
            partition_label = None if partition_label_match == None else partition_label_match.group(1)

            if disk in partitions:
                partitions[disk].type = partition_type
                partitions[disk].label = partition_label
                partitions[disk].size = disk_size
                disks[-1].partitions.append(partitions[disk])
            else:
                disks[-1].partitions.append(Partition(disk, f'/dev/disk/by-uuid/{re.search('UUID="([^"]+)"', blkid).group(1)}', [], partition_type, disk_size, partition_label))
            
            continue
        
        disks.append(Disk(disk, [], disk_size))

    return disks
