class Partition:
    path: str
    mount_points: list[str]
    uuid_path: str
    type: str
    size: int
    label: str | None

    def __init__(self, path, uuid_path, mount_points, type, size, label = None):
        self.path = path
        self.uuid_path = uuid_path
        self.mount_points = mount_points
        self.type = type
        self.size = size
        self.label = label
