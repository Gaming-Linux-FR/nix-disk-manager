def parse_proc_disks():
    content = []

    with open('/proc/partitions', 'r') as proc_file:
        content = proc_file.readlines()

    content = content[2:]
    
    disks = []

    for disk_line in content:
        disk = '/dev/' + disk_line.split(' ')[-1].strip()
        
        if len(disks) > 0 and disk.startswith(disks[-1]):
            continue
        
        disks.append(disk)

    return disks