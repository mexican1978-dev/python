class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_d(self):
        return self.width / 6.5 + 0.5

    def get_square_v(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Square all cloth \n {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Dress(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_d = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Square on dress {self.square_d}'


class Vest(Cloth):
    def __init__(self, width, height):
        super(). __init__(width, height)
        self.square_v = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Square on vest {self.square_v}'


dress = Dress(2, 4)
vest = Vest(1, 2)
print(dress)
print(vest)
print(dress.get_sq_full)
print(vest.get_sq_full)
print(dress.get_square_d())
print(vest.get_square_v())
