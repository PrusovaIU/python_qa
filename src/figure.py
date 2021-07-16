from abc import ABCMeta, abstractmethod
from typing import List


class FigureCreateError(Exception):
    def __init__(self, text_err: str):
        self.__name = "Can not create the figure"
        self.__txt = text_err

    def __str__(self):
        return f"{self.__name}: {self.__txt}"


class Figure(metaclass=ABCMeta):
    def __init__(self, sides: List[float]):
        """
        :param sides: lengths figure's sides
        :return: None or raise FigureCreatingError
        """
        try:
            assert len(sides) > 0, "Length of sides have not been set"
            self.__sides: List[float] = sides
        except AssertionError as err:
            raise FigureCreateError(str(err))

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def sides(self) -> List[float]:
        return self.__sides

    def add_area(self, added_figure) -> float:
        """
        Add area of added_figure to self area
        :param added_figure: instance of class Figure
        :return: return summarised area or raise ValueError
        """
        if not isinstance(added_figure, Figure):
            raise ValueError(f"Class \"Figure\" is required, but \"{type(added_figure)}\" has been got")
        return self.area() + added_figure.area()

    @abstractmethod
    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        perimeter = 0
        for side in self.__sides:
            perimeter += side
        return perimeter
