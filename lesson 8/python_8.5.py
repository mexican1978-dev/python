class ComNum:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + y * i'

    def __add__(self, other):
        return f'Sum z1 и z2 = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        return f'Multiply z1 и z2 = {self.x * other.x - (self.y * other.y)} + {self.y * other.y} * i'

    def __str__(self):
        return f'z = {self.x} + {self.x} * i'


z_1 = ComNum(1, -2)
z_2 = ComNum(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
