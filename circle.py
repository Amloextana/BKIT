from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import FigureColor
import math


class Circle(GeometricFigure):

    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radius, color_param):
        self.radius = radius
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def calculate_square(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '\nНазвание фигуры: {}\nРадиус: {}\nПлощадь: {}\nЦвет: {}'.format(
            Circle.get_figure_type(),
            self.radius,
            round(self.calculate_square(), 1),
            self.fc.colorproperty
        )

