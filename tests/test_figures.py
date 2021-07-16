from .help import float_format
from src.circle import Circle
from src.figure import Figure
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
import pytest


CIRCLE_REQUIRED_AREA = 314.159
RECTANGLE_REQUIRED_AREA = 2
SQUIRE_REQUIRED_AREA = 25
TRIANGLE_REQUIRED_AREA = 16.248


CIRCLE_REQUIRED_PERIMETER = 62.831
RECTANGLE_REQUIRED_PERIMETER = 6
SQUIRE_REQUIRED_PERIMETER = 20
TRIANGLE_REQUIRED_PERIMETER = 22


def circle() -> Circle:
    return Circle(10)


def rectangle() -> Rectangle:
    return Rectangle(1, 2)


def squire() -> Square:
    return Square(5)


def triangle() -> Triangle:
    return Triangle(5, 7, 10)


@pytest.mark.parametrize("figure, figure_area",
                         [(circle(), CIRCLE_REQUIRED_AREA),
                          (rectangle(), RECTANGLE_REQUIRED_AREA),
                          (squire(), SQUIRE_REQUIRED_AREA),
                          (triangle(), TRIANGLE_REQUIRED_AREA)])
def test_add_area(figure: Figure, figure_area: float):

    def check_add_area(added_figure: Figure, added_figure_area: float):
        summarised_area = figure.add_area(added_figure)
        assert float_format(summarised_area) == float_format(figure_area + added_figure_area)

    check_add_area(circle(), CIRCLE_REQUIRED_AREA)
    check_add_area(rectangle(), RECTANGLE_REQUIRED_AREA)
    check_add_area(squire(), SQUIRE_REQUIRED_AREA)
    check_add_area(triangle(), TRIANGLE_REQUIRED_AREA)


@pytest.mark.parametrize("figure", [circle(), rectangle(), squire(), triangle()])
def test_add_area_error(figure: Figure):
    with pytest.raises(ValueError):
        figure.add_area([10, 10, 10])


@pytest.mark.parametrize("figure, required_area",
                         [(circle(), CIRCLE_REQUIRED_AREA),
                          (rectangle(), RECTANGLE_REQUIRED_AREA),
                          (squire(), SQUIRE_REQUIRED_AREA),
                          (triangle(), TRIANGLE_REQUIRED_AREA)])
def test_area(figure: Figure, required_area: float):
    assert float_format(figure.area()) == float_format(required_area)


@pytest.mark.parametrize("figure, required_perimeter",
                         [(circle(), CIRCLE_REQUIRED_PERIMETER),
                          (rectangle(), RECTANGLE_REQUIRED_PERIMETER),
                          (squire(), SQUIRE_REQUIRED_PERIMETER),
                          (triangle(), TRIANGLE_REQUIRED_PERIMETER)])
def test_perimeter(figure: Figure, required_perimeter: float):
    perimeter = figure.perimeter()
    assert float_format(perimeter) == float_format(required_perimeter)
