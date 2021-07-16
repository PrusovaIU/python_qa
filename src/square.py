from .figure import Figure


class Square(Figure):
    name = "square"

    def __init__(self, side: float):
        super(Square, self).__init__([side])

    def area(self) -> float:
        return self.sides[0] ** 2
