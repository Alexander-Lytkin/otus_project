from src.Figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        self.a = a

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return self.a * 4

    def __repr__(self):
        return f"Квадрат со стороной {self.a}, периметром {self.perimeter}, площадью {self.area}"
