from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b)*2

    def __repr__(self):
        return f"Прямоугольник со сторонами {self.a}, {self.b} периметром {self.perimeter}, площадью {self.area}"
