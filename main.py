from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import unittest
import numpy


class FiguresTests(unittest.TestCase):

    def test_rectangle(self):
        rectangle_test = Rectangle(13, 13, "Синий")
        self.assertEqual(repr(rectangle_test),
                        "\nНазвание фигуры: Прямоугольник\nДлинна: 13\nШирина: 13\nПлощадь: 169\nЦвет: Синий")

    def test_circle(self):
        circle_test = Circle(13, "Зеленый")
        self.assertEqual(repr(circle_test),
                            "\nНазвание фигуры: Круг\nРадиус: 13\nПлощадь: 530.9\nЦвет: Зеленый")

    def test_square(self):
        square_test = Square(13, "Красный")
        self.assertEqual(repr(square_test),
                            "\nНазвание фигуры: Квадрат\nДлинна: 13\nПлощадь: 169\nЦвет: Красный")





if __name__ == "__main__":

    r = Rectangle(13, 13, "Синий")
    c = Circle(13, "Зеленый")
    s = Square(13, "Красный")
    print(r)
    print(c)
    print(s)

    unittest.main()

