import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Круг с радиусом {self.radius} периметром {self.perimeter}, площадью {self.area}"
