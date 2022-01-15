def test_calculate_triangle_area(triangle):
    assert triangle.area == 84


def tests_calculate_triangle_perimeter(triangle):
    assert triangle.perimeter == 42


def tests_add_triangle_area_to_triangle(square, triangle):
    assert triangle.add_area(square) == 184


def test_triangle_name(triangle):
    assert triangle.name == "Треугольник"


def tests_send_wrong_figure_to_add_area(triangle):
    try:
        triangle.add_area("INVALID_FIGURE")
    except ValueError as exc:
        assert exc.args[0] == "Передан неправильный класс"
