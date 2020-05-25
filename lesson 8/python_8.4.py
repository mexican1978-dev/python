class OfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price}  {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Enter model: ')
            unit_p = int(input(f'Enter price: '))
            unit_q = int(input(f'Enter quantity: '))
            unique = {'Model': unit, 'Price': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current list -\n {self.my_store}')
        except:
            return f'Error!!!'

        print(f' List - Q, Continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'List -\n {self.my_store_full}')
            return f'Exit'
        else:
            return OfficeEquipment.reception(self)


class Printer(OfficeEquipment):
    def to_print(self):
        return f'to print in {self.numb} times'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'to scan in {self.numb} times'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'to copier in {self.numb} times'


unit_1 = Printer('HP', 5000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
