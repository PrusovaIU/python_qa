from src.triangle import Triangle, FigureCreateError
import pytest


def test_error_creating():
    with pytest.raises(FigureCreateError):
        Triangle(1, 2, 3)
