import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        p = self.perimeter / 2
        return int(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def half_perimeter(self):
        return self.perimeter / 2

    def __repr__(self):
        return f"Треугольник со сторонами {self.a}, {self.b}, {self.c}," \
               f" периметром {self.perimeter}, площадью {self.area}"
