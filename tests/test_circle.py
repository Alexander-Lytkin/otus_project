def test_calculate_circle_area(circle):
    assert circle.area == 314.1592653589793


def tests_calculate_circle_perimeter(circle):
    assert circle.perimeter == 62.83185307179586


def tests_add_triangle_area_to_circle(circle, triangle):
    assert circle.add_area(triangle) == 398.1592653589793


def test_get_circle_name(circle):
    assert circle.name == "Круг"


def tests_send_wrong_figure_to_add_area(circle):
    try:
        circle.add_area("INVALID_FIGURE")
    except ValueError as exc:
        assert exc.args[0] == "Передан неправильный класс"
