import unittest
from rectangles import *


class TestRectangle(unittest.TestCase):
    def test__str__(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).__str__(), "[(0, 0), (4, 4)]")
        self.assertEqual(Rectangle(-2, -2, 2, 2).__str__(),  "[(-2, -2), (2, 2)]")
        self.assertEqual(Rectangle(0, -5, 4, 5).__str__(),  "[(0, -5), (4, 5)]")
        self.assertEqual(Rectangle(9, 9, 10, 10).__str__(),  "[(9, 9), (10, 10)]")

    def test__repr__(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).__repr__(), "Rectangle(0, 0, 4, 4)")
        self.assertEqual(Rectangle(-2, -2, 2, 2).__repr__(), "Rectangle(-2, -2, 2, 2)")
        self.assertEqual(Rectangle(0, -5, 4, 5).__repr__(), "Rectangle(0, -5, 4, 5)")
        self.assertEqual(Rectangle(9, 9, 10, 10).__repr__(), "Rectangle(9, 9, 10, 10)")

    def test__eq__(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).__eq__(Rectangle(0, 0, 4, 4)),True)
        self.assertEqual(Rectangle(-2, -2, 2, 2).__eq__(Rectangle(2, 2, -2, -2)), False)
        self.assertEqual(Rectangle(0, -5, 4, 5).__eq__(Rectangle(0, 5, 4, 5)), False)
        self.assertEqual(Rectangle(9, 9, 10, 10).__eq__(Rectangle(10, 10, 10, 10)), False)

    def test__ne__(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).__ne__(Rectangle(0, 0, 4, 4)), False)
        self.assertEqual(Rectangle(-2, -2, 2, 2).__ne__(Rectangle(2, 2, -2, -2)), True)
        self.assertEqual(Rectangle(0, -5, 4, 5).__ne__(Rectangle(0, 5, 4, 5)), True)
        self.assertEqual(Rectangle(9, 9, 10, 10).__ne__(Rectangle(10, 10, 10, 10)), True)

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).center(), (2, 2))
        self.assertEqual(Rectangle(-2, -2, 2, 2).center(), (0, 0))
        self.assertEqual(Rectangle(0, -5, 4, 5).center(), (2, 0))
        self.assertEqual(Rectangle(9, 9, 10, 10).center(), (9.5, 9.5))
        self.assertEqual(Rectangle(2, 3, 5, 6).center(), (3.5, 4.5))
        self.assertEqual(Rectangle(2, 5, 6, 10).center(), (4, 7.5))
        self.assertEqual(Rectangle(0, 1, 3, 2).center(), (1.5, 1.5))
        self.assertEqual(Rectangle(5, 5, 0, 2).center(), (2.5, 3.5))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).area(), 16)
        self.assertEqual(Rectangle(-2, -2, 2, 2).area(), 16)
        self.assertEqual(Rectangle(0, -5, 4, 5).area(), 40)
        self.assertEqual(Rectangle(9, 9, 10, 10).area(), 1)
        self.assertEqual(Rectangle(2, 3, 5, 6).area(), 9)
        self.assertEqual(Rectangle(2, 5, 6, 10).area(), 20)
        self.assertEqual(Rectangle(0, 1, 3, 2).area(), 3)
        self.assertEqual(Rectangle(5, 5, 0, 2).area(), 15)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).move(1, 0), (1, 0, 5, 4))
        self.assertEqual(Rectangle(-2, -2, 2, 2).move(2, 2), (0, 0, 4, 4))
        self.assertEqual(Rectangle(0, -5, 4, 5).move(0, -3), (0, -8, 4, 2))
        self.assertEqual(Rectangle(9, 9, 10, 10).move(2, 10), (11, 19, 12, 20))
        self.assertEqual(Rectangle(2, 3, 5, 6).move(2.5, 3.5), (4.5, 6.5, 7.5, 9.5))
        self.assertEqual(Rectangle(2, 5, 6, 10).move(-1, -1), (1, 4, 5, 9))
        self.assertEqual(Rectangle(0, 1, 3, 2).move(0, 0), (0, 1, 3, 2))
        self.assertEqual(Rectangle(5, 5, 0, 2).move(-10, 10), (-5, 15, -10, 12))

if __name__ == '__main__':
    unittest.main()
