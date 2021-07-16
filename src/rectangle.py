from .figure import Figure


class Rectangle(Figure):
    name = "rectangle"

    def __init__(self, length: float, width: float):
        super(Rectangle, self).__init__([length, width] * 2)

    def area(self) -> float:
        return self.sides[0] * self.sides[1]
