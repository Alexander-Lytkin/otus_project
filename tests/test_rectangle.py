def test_calculate_rectangle_area(rectangle):
    assert rectangle.area == 150


def tests_calculate_rectangle_perimeter(rectangle):
    assert rectangle.perimeter == 50


def tests_add_rectangle_area_to_circle(rectangle, square):
    assert rectangle.add_area(square) == 250


def test_get_rectangle_name(rectangle):
    assert rectangle.name == "Прямоугольник"


def tests_send_wrong_figure_to_add_area(rectangle):
    try:
        rectangle.add_area("INVALID_FIGURE")
    except ValueError as exc:
        assert exc.args[0] == "Передан неправильный класс"
