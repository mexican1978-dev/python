class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def cover_road(self):
        return self._length * self._width


class asphalt(Road):
    def __init__(self, _length, _width,  mass, volume):
        super().__init__(_length, _width)
        self.volume = volume
        self.mass = mass

    def cover_road(self):
        return self._length * self._width * self.volume * self.mass


r = asphalt(20, 5000, 25, 5)
print(r.cover_road())
