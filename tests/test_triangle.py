from .help import float_format
from src.triangle import Triangle, FigureCreateError
import pytest


REQUIRED_AREA = 16.248


@pytest.fixture()
def triangle() -> Triangle:
    return Triangle(5, 7, 10)


# def test_add_area(triangle):
#     summarised_area = triangle.add_area(triangle)
#     assert float_format(summarised_area) == float_format(2 * REQUIRED_AREA)
#
#
# def test_area(triangle):
#     area = float_format(triangle.area())
#     assert area == REQUIRED_AREA


def test_error_creating():
    with pytest.raises(FigureCreateError):
        Triangle(1, 2, 3)


# def test_name(triangle):
#     assert triangle.name is not None, "There is not NAME"
# 
#
# def test_perimeter(triangle):
#     assert triangle.perimeter() == 5 + 7 + 10
