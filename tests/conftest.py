import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture()
def circle():
    circle = Circle(10)
    circle.name = "Круг"
    yield circle
    del circle


@pytest.fixture()
def rectangle():
    rectangle = Rectangle(10, 15)
    rectangle.name = "Прямоугольник"
    yield rectangle
    del rectangle


@pytest.fixture()
def square():
    square = Square(10)
    square.name = "Квадрат"
    yield square
    del square


@pytest.fixture()
def triangle():
    triangle = Triangle(13, 14, 15)
    triangle.name = "Треугольник"
    yield triangle
    del triangle
