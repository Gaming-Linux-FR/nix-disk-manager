from nixdiskmanager.utils.partition import Partition

class Disk:
    path: str
    partitions: list[Partition]
    size: int

    def __init__(self, path, partitions, size):
        self.path = path
        self.partitions = partitions
        self.size = size