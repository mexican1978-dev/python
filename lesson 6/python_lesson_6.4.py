class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started!'

    def stop(self):
        return f'{self.name} is stopped!'

    def turn_right(self):
        return f'{self.name} is turned right!'

    def turn_left(self):
        return f'{self.name} is turned left!'

    def show_speed(self):
        return f'Speed {self.name} is {self.speed}!'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Town's car {self.name} speed is {self.speed}")

        if self.speed > 40:
            return f'Speed {self.name} is HIGH!!!'
        else:
            return f'Speed {self.name} is OK!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Work's car {self.name} speed is {self.speed}")

        if self.speed > 60:
            return f'Speed {self.name} is HIGH!!!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} in police.'
        else:
            return f'{self.name} not in police.'


ferrari = SportCar(200, 'Red', 'Ferrari', False)
mini_cooper = TownCar(60, 'Brown', 'Mini cooper', False)
fiat = WorkCar(80, 'Black', 'Fiat', True)
pontiac = PoliceCar(180, 'White-Blue', 'Pontiac', True)
print(pontiac.turn_left())

print(f'{ferrari.name} is {ferrari.color}')
print(f'{pontiac.name} in police? {pontiac.is_police}!')
print(mini_cooper.show_speed())
print(fiat.show_speed())
print(ferrari.show_speed())
print(pontiac.show_speed())
print(ferrari.stop())
print(pontiac.stop())
print(mini_cooper.stop())
print(fiat.stop())
print(f'{fiat.turn_right()} and {ferrari.turn_left()}')
print(f'{fiat.turn_left()} and {ferrari.turn_right()}')
