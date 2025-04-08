from nixdiskmanager.utils.partition import Partition

class Disk:
    path: str
    partitions: list[Partition]

    def __init__(self, path, partitions):
        self.path = path
        self.partitions = partitions