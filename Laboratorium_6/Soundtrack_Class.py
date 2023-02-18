class Soundtrack:
    def __init__(self,id, time, artist, title):
        self.id = id
        self.time = time
        self.artist = artist
        self.title = title

    def __lt__(self, other):
        return self.artist < other.artist
       