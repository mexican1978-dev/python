class DivByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except:
            return f'Divide by zero error encountered.'


div = DivByNull(10, 100)
print(DivByNull.divide_by_null(10, 0))
print(DivByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))