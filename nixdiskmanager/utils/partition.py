class Partition:
    path: str
    mount_points: list[str]
    uuid_path: str
    type: str

    def __init__(self, path, uuid_path, mount_points, type):
        self.path = path
        self.uuid_path = uuid_path
        self.mount_points = mount_points
        self.type = type
