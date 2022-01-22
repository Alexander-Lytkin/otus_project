class Figure:
    def __init__(self, name: str):
        self.__name = name
        self.__area = 0
        self.__perimeter = 0

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            raise ValueError("Передан неправильный класс")

    @property
    def name(self):
        return self.__name

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    @name.setter
    def name(self, value):
        self.__name = value

    @area.setter
    def area(self, value):
        self.__area = value

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value
