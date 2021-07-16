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
    def __check_creating_condition(first_side: float, second_side: float, third_side: float) -> None:
        """
        Check whether a triangle creating with a required sides is possible
        :param first_side: length of first side
        :param second_side: length of second side
        :param third_side: length of third side
        :return: None or raise AssertionError
        """
        assert first_side + second_side > third_side or \
               second_side + third_side > first_side or \
               first_side + third_side > second_side, \
               f"There is not a triangle with the sides {first_side}, {second_side}, {third_side}"

    def area(self) -> float:
        p = self.perimeter()/2
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[3]
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
