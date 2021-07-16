from .figure import Figure, FigureCreateError


class Triangle(Figure):
    name = "triangle"

    def __init__(self, first_side: float, second_side: float, third_side: float):
        """
        :param first_side: length of first side
        :param second_side: length of second side
        :param third_side: length of third side
        :return: None or raise FigureCreatingError
        """
        try:
            self.__check_creating_condition(first_side, second_side, third_side)
            super(Triangle, self).__init__([first_side, second_side, third_side])
        except AssertionError as err:
            raise FigureCreateError(str(err))

    @staticmethod
    def __check_creating_condition(a: float, b: float, c: float) -> None:
        """
        Check whether a triangle creating with a required sides is possible
        :param a: length of first side
        :param b: length of second side
        :param c: length of third side
        :return: None or raise AssertionError
        """
        assert a + b > c and \
               b + c > a and \
               a + c > b, \
               f"There is not a triangle with the sides {a}, {b}, {c}"

    def area(self) -> float:
        p = self.perimeter()/2
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
