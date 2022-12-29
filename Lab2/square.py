from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):

    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):

        return cls.FIGURE_TYPE

    def __init__(self, side_param, color_param):
        """
        Класс должен содержать конструктор по параметрам «сторона» и «цвет».
        """
        self.side = side_param
        super().__init__(self.side, self.side, color_param)

    def calculate_square(self):
        return self.side ** 2

    def __repr__(self):
        return '\nНазвание фигуры: {}\nДлинна: {}\nПлощадь: {}\nЦвет: {}'.format(
            Square.get_figure_type(),
            self.side,
            self.calculate_square(),
            self.fc.colorproperty
        )
