from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import FigureColor


class Rectangle(GeometricFigure):

    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, length, width, color_param):
        self.length = length
        self.width = width
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def calculate_square(self):
        return self.width * self.length

    def __repr__(self):
        return '\nНазвание фигуры: {}\nДлинна: {}\nШирина: {}\nПлощадь: {}\nЦвет: {}'.format(
            Rectangle.get_figure_type(),
            self.length,
            self.width,
            self.calculate_square(),
            self.fc.colorproperty
        )
