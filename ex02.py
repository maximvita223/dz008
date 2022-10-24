class Clothes:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани'
                   f' {round((self.width / 6.5 + 0.5)) + (self.height * 2 + 0.3)}')


class CoatJacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5, 2)
        self.square_j = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Площадь на пальто {self.square_c} \n' f'Площадь на костюм {self.square_j}'


coat = CoatJacket(2, 4)
print(coat)
print(coat.get_sq_full)
