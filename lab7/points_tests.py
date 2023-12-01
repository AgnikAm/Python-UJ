import unittest
from points import *


class TestPoint(unittest.TestCase):
    def test__str__(self):
        self.assertEqual(Point(0, 0).__str__(), "(0, 0)")
        self.assertEqual(Point(-7.5, 0).__str__(),  "(-7.5, 0)")
        self.assertEqual(Point(0, -5).__str__(),  "(0, -5)")
        self.assertEqual(Point(9, 9.2).__str__(),  "(9, 9.2)")

    def test__repr__(self):
        self.assertEqual(Point(0, 0).__repr__(), "Point(0, 0)")
        self.assertEqual(Point(-7, 0).__repr__(),  "Point(-7, 0)")
        self.assertEqual(Point(0, -5).__repr__(),  "Point(0, -5)")
        self.assertEqual(Point(9, 9).__repr__(),  "Point(9, 9)")

    def test__eq__(self):
        self.assertEqual(Point(0, 0).__eq__(Point(0, 0)), True)
        self.assertEqual(Point(-7, 0).__eq__(Point(0, 0)),  False)
        self.assertEqual(Point(0, -5).__eq__(Point(0, 0)),  False)
        self.assertEqual(Point(9, 9).__eq__(Point(0, 0)),  False)

    def test__ne__(self):
        self.assertEqual(Point(0, 0).__ne__(Point(0, 0)), False)
        self.assertEqual(Point(-7, 0).__ne__(Point(0, 0)),  True)
        self.assertEqual(Point(0, -5).__ne__(Point(0, 0)),  True)
        self.assertEqual(Point(9, 9).__ne__(Point(0, 0)),  True)

    def test__add__(self):
        self.assertEqual(Point(0, 0).__add__(Point(0, 0)), Point(0, 0))
        self.assertEqual(Point(-7, 0).__add__(Point(0, 0)),  Point(-7, 0))
        self.assertEqual(Point(0, -5).__add__(Point(0, 0)),  Point(0, -5))
        self.assertEqual(Point(9, 9).__add__(Point(0, 0)),  Point(9, 9))
        self.assertEqual(Point(9, 9).__add__(Point(-2, -1)), Point(7, 8))
        self.assertEqual(Point(0, -5).__add__(Point(3, -5)), Point(3, -10))
        self.assertEqual(Point(3, -5).__add__(Point(-2, 1)), Point(1, -4))
        self.assertEqual(Point(-8, 12).__add__(Point(5, -3)), Point(-3, 9))
        self.assertEqual(Point(1, -1).__add__(Point(-1, 1)), Point(0, 0))


    def test__sub__(self):
        self.assertEqual(Point(0, 0).__sub__(Point(0, 0)), Point(0, 0))
        self.assertEqual(Point(-7, 0).__sub__(Point(0, 0)),  Point(-7, 0))
        self.assertEqual(Point(0, -5).__sub__(Point(0, 0)),  Point(0, -5))
        self.assertEqual(Point(9, 9).__sub__(Point(0, 0)),  Point(9, 9))
        self.assertEqual(Point(9, 9).__sub__(Point(-2, -1)), Point(11, 10))
        self.assertEqual(Point(0, -5).__sub__(Point(3, -5)), Point(-3, 0))
        self.assertEqual(Point(3, -5).__sub__(Point(-2, 1)), Point(5, -6))
        self.assertEqual(Point(-8, 12).__sub__(Point(5, -3)), Point(-13, 15))
        self.assertEqual(Point(1, -1).__sub__(Point(-1, 1)), Point(2, -2))

    def test__mul__(self):
        self.assertEqual(Point(0, 0).__mul__(Point(0, 0)), 0)
        self.assertEqual(Point(-7, 0).__mul__(Point(0, 0)), 0)
        self.assertEqual(Point(0, -5).__mul__(Point(0, 0)), 0)
        self.assertEqual(Point(9, 9).__mul__(Point(0, 0)), 0)
        self.assertEqual(Point(9, 9).__mul__(Point(-2, -1)), -27)
        self.assertEqual(Point(0, -5).__mul__(Point(3, -5)), 25)
        self.assertEqual(Point(2, -10).__mul__(Point(-2, -1)), 6)
        self.assertEqual(Point(1, -25).__mul__(Point(-3, 5)), -128)
        self.assertEqual(Point(9, 9).__mul__(Point(2, 3)), 45)
        self.assertEqual(Point(2, -10).__mul__(Point(2, 1)), -6)

    def test_cross(self):
        self.assertEqual(Point(0, 0).cross(Point(0, 0)), 0)
        self.assertEqual(Point(-7, 0).cross(Point(0, 0)), 0)
        self.assertEqual(Point(0, -5).cross(Point(0, 0)), 0)
        self.assertEqual(Point(9, 9).cross(Point(0, 0)), 0)
        self.assertEqual(Point(9, 9).cross(Point(-2, -1)), 9)
        self.assertEqual(Point(0, -5).cross(Point(3, -5)), 15)
        self.assertEqual(Point(2, -10).cross(Point(-2, -1)), -22)
        self.assertEqual(Point(1, -25).cross(Point(-3, 5)), -70)
        self.assertEqual(Point(9, 9).cross(Point(2, 3)), 9)
        self.assertEqual(Point(2, -10).cross(Point(2, 1)), 22)

    def test_length(self):
        self.assertEqual(Point(0, 0).length(), 0)
        self.assertEqual(Point(-7, 0).length(), 7)
        self.assertEqual(Point(0, -5).length(), 5)
        self.assertEqual(round(Point(9, 9).length(), 1), 12.7)
        self.assertEqual(round(Point(2, -5).length(), 1), 5.4)
        self.assertEqual(round(Point(10, -7).length(), 1), 12.2)
        self.assertEqual(round(Point(-9, -1).length(), 1), 9.1)
        self.assertEqual(round(Point(2, 2).length(), 1), 2.8)
        self.assertEqual(round(Point(3, -6).length(), 1), 6.7)

    def test__hash__(self):
        self.assertEqual(hash(Point(3, 5)), hash((3, 5)))
        self.assertEqual(hash(Point(-7, 0)), hash((-7, 0)))
        self.assertEqual(hash(Point(0, -5)), hash((0, -5)))
        self.assertEqual(hash(Point(9, 9)), hash((9, 9)))
        self.assertEqual(hash(Point(-23, -25)), hash((-23, -25)))
        self.assertEqual(hash(Point(10, 1)), hash((10, 1)))
        self.assertEqual(hash(Point(-4, -5)), hash((-4, -5)))
        self.assertEqual(hash(Point(0, 0)), hash((0, 0)))

        self.assertNotEqual(hash(Point(3, 5)), hash((-7, 0)))
        self.assertNotEqual(hash(Point(3, 5)), hash((0, -5)))
        self.assertNotEqual(hash(Point(3, 5)), hash((9, 9)))
        self.assertNotEqual(hash(Point(3, 5)), hash((-23, -23)))
        self.assertNotEqual(hash(Point(3, 5)), hash((10, 1)))
        self.assertNotEqual(hash(Point(3, 5)), hash((-4, -5)))
        self.assertNotEqual(hash(Point(3, 5)), hash((0, 0)))
        self.assertNotEqual(hash(Point(3, 5)), hash((-16, -1)))
        self.assertNotEqual(hash(Point(3, 5)), hash((5, 3)))



if __name__ == '__main__':
    unittest.main()
