def parse_size(size_bits) -> str:
    if size_bits < 1_000_000_000:
        disk_size_label = f'{int(size_bits / 1_000_000)}M'
    else:
        disk_size_label = f'{int(size_bits / 1_000_000_000)}G'

    return disk_size_label