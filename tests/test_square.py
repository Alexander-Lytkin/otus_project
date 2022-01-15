def test_calculate_square_area(square):
    assert square.area == 100


def tests_calculate_square_perimeter(square):
    assert square.perimeter == 40


def tests_add_square_area_to_triangle(square, triangle):
    assert square.add_area(triangle) == 184


def test_square_name(square):
    assert square.name == "Квадрат"


def tests_send_wrong_figure_to_add_area(square):
    try:
        square.add_area("INVALID_FIGURE")
    except ValueError as exc:
        assert exc.args[0] == "Передан неправильный класс"
