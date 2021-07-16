from .figure import Figure
from math import pi


class Circle(Figure):
    name = "circle"

    def __init__(self, radius: float):
        super(Circle, self).__init__([radius])

    def area(self) -> float:
        return pi * (self.sides[0] ** 2)

    def perimeter(self) -> float:
        return 2 * pi * self.sides[0]
