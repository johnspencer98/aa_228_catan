class Edge:
    def __init__(self):
        self.coordinate = None
        self.player = None
        self.vertices = []

    def to_string(self):
        if self.player is None:
            return str(self.coordinate)
        else:
            return self.player
