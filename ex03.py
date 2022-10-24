class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return Cell(self.quantity - other.quantity)
        else:
            print('Отрицательно!')


    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def __str__(self):
        return f'Результат операции {self.quantity * "*"} - {self.quantity} ячеек'

cells1 = Cell(33)
cells2 = Cell(9)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells1 / cells2)
