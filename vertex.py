class Vertex:
    def __init__(self):
        self.coordinate = None
        self.type = 'empty'
        self.player = None
        self.edges = []
        self.tiles = []

    def to_string(self):
        if self.player is None:
            return str(self.coordinate)
        else:
            return self.player + ':' + self.type
