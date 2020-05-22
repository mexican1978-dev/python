class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Draw with {self.title}')


class Pen(Stationary):

    def draw(self):
        return f'You take a {self.title}. Draw with a pen!'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You take a {self.title}. Draw with a pencil!'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You take a {self.title}. Draw with a handle!'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
