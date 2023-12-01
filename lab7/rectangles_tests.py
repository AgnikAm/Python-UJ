import unittest
from rectangles import *


class TestRectangle(unittest.TestCase):

    def test_invalid_coordinates(self):
        # Test when coordinates are invalid
        with self.assertRaises(ValueError) as context:
            invalid_rectangle = Rectangle(3, 4, 1, 2)

        self.assertEqual(str(context.exception),
                         "Wrong coordinates. x1 must be smaller than x2 and y1 must be smaller than y2")

    def test__str__(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).__str__(), "[(0, 0), (4, 4)]")
        self.assertEqual(Rectangle(9, 9, 10, 10).__str__(),  "[(9, 9), (10, 10)]")
        self.assertEqual(Rectangle(-3, 2, -1, 9).__str__(), "[(-3, 2), (-1, 9)]")
        self.assertEqual(Rectangle(4, -2, 6, 10).__str__(), "[(4, -2), (6, 10)]")

    def test__repr__(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).__repr__(), "Rectangle(0, 0, 4, 4)")
        self.assertEqual(Rectangle(9, 9, 10, 10).__repr__(), "Rectangle(9, 9, 10, 10)")

    def test__eq__(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).__eq__(Rectangle(0, 0, 4, 4)),True)
        self.assertEqual(Rectangle(9, 9, 10, 10).__eq__(Rectangle(10, 10, 12, 12)), False)

    def test__ne__(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).__ne__(Rectangle(0, 0, 4, 4)), False)
        self.assertEqual(Rectangle(9, 9, 10, 10).__ne__(Rectangle(10, 10, 12, 12)), True)

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).center(), Point(2, 2))
        self.assertEqual(Rectangle(9, 9, 10, 10).center(), Point(9.5, 9.5))
        self.assertEqual(Rectangle(2, 3, 5, 6).center(), Point(3.5, 4.5))
        self.assertEqual(Rectangle(2, 5, 6, 10).center(), Point(4, 7.5))
        self.assertEqual(Rectangle(0, 1, 3, 2).center(), Point(1.5, 1.5))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).area(), 16)
        self.assertEqual(Rectangle(9, 9, 10, 10).area(), 1)
        self.assertEqual(Rectangle(2, 3, 5, 6).area(), 9)
        self.assertEqual(Rectangle(2, 5, 6, 10).area(), 20)
        self.assertEqual(Rectangle(0, 1, 3, 2).area(), 3)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).move(1, 0), Rectangle(1, 0, 5, 4))
        self.assertEqual(Rectangle(9, 9, 10, 10).move(2, 10), Rectangle(11, 19, 12, 20))
        self.assertEqual(Rectangle(2, 3, 5, 6).move(2.5, 3.5), Rectangle(4.5, 6.5, 7.5, 9.5))
        self.assertEqual(Rectangle(2, 5, 6, 10).move(-1, -1), Rectangle(1, 4, 5, 9))
        self.assertEqual(Rectangle(0, 1, 3, 2).move(0, 0), Rectangle(0, 1, 3, 2))

    def test_intersection(self):
        self.assertEqual(Rectangle(2,3, 6, 7).intersection(Rectangle(3, 5, 7, 9)), Rectangle(3, 5, 6, 7))
        self.assertEqual(Rectangle(-9, -3, -4, -1).intersection(Rectangle(-8, -4, -5, 1)), Rectangle(-8, -3, -5, -1))
        self.assertEqual(Rectangle(-4, -1, 1, 3).intersection(Rectangle(0, -4, 3, 0)), Rectangle(0, -1, 1, 0))
        self.assertEqual(Rectangle(-3, -2, 3, 2).intersection(Rectangle(-2, -1, 0, 2)), Rectangle(-2, -1, 0, 2))
        self.assertEqual(Rectangle(-9, -3, -4, -1).intersection(Rectangle(2, 3, 5, 7)), None)

    def test_cover(self):
        self.assertEqual(Rectangle(2,3, 6, 7).cover(Rectangle(3, 5, 7, 9)), Rectangle(2, 3, 7, 9))
        self.assertEqual(Rectangle(-9, -3, -4, -1).cover(Rectangle(-8, -4, -5, 1)), Rectangle(-9, -4, -4, 1))
        self.assertEqual(Rectangle(-4, -1, 1, 3).cover(Rectangle(0, -4, 3, 0)), Rectangle(-4, -4, 3, 3))
        self.assertEqual(Rectangle(-3, -2, 3, 2).cover(Rectangle(-2, -1, 0, 2)), Rectangle(-3, -2, 3, 2))
        self.assertEqual(Rectangle(-9, -3, -4, -1).cover(Rectangle(2, 3, 5, 7)), Rectangle(-9, -3, 5, 7))

    def make4(self):
        self.assertEqual(Rectangle(2,3, 6, 7).make4(),
                                                     Rectangle(2, 3, 4, 5),
                                                     Rectangle(2, 5, 4, 7),
                                                     Rectangle(4, 5, 6, 7),
                                                     Rectangle(4, 3, 6, 5))

        self.assertEqual(Rectangle(-3, -2, 1, 5).make4(),
                                                     Rectangle(-3, -2, -1, 1.5),
                                                     Rectangle(-3, 1.5, -1, 5),
                                                     Rectangle(-1, 1.5, 1, 5),
                                                     Rectangle(-1, -2, 1, 1.5))

        self.assertEqual(Rectangle(0, 2, 4, 6).make4(),
                                                     Rectangle(0, 2, 2, 4),
                                                     Rectangle(0, 4, 2, 6),
                                                     Rectangle(2, 4, 4, 6),
                                                     Rectangle(2, 2, 4, 4))

        self.assertEqual(Rectangle(-3, -2, 3, 2).make4(),
                                                     Rectangle(-3, -2, 0, 0),
                                                     Rectangle(-3, 0, 0, 2),
                                                     Rectangle(0, 0, 3, 2),
                                                     Rectangle(0, -2, 3, 0))


if __name__ == '__main__':
    unittest.main()
