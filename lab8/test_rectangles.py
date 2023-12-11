import pytest
from rectangles import *
from points import *

def set_points_A():
    point1 = Point(2, 3)
    point2 = Point(6, 7)
    return point1, point2

def set_points_B():
    point1 = Point(-8, -4)
    point2 = Point(-5, -1)
    return point1, point2

def set_points_C():
    point1 = Point(-3, -2)
    point2 = Point(3, 2)
    return point1, point2

@pytest.mark.parametrize("set_points", [set_points_A, set_points_B, set_points_C])
def test_from_points(set_points):
    point1, point2 = set_points()
    rectangle = Rectangle.from_points((point1, point2))
    assert rectangle.pt1 == point1
    assert rectangle.pt2 == point2

def test_attributesA():
    rectangle = Rectangle(2, 3, 6, 7)
    assert rectangle.top == 7
    assert rectangle.left == 2
    assert rectangle.bottom == 3
    assert rectangle.right == 6
    assert rectangle.width == 4
    assert rectangle.height == 4
    assert rectangle.topleft == Point(2, 7)
    assert rectangle.bottomleft == Point(2, 3)
    assert rectangle.topright == Point(6, 7)
    assert rectangle.bottomright == Point(6, 3)
    assert rectangle.center == Point(4, 5)

def test_attributesB():
    rectangle = Rectangle(-8, -4, -5, -1)
    assert rectangle.top == -1
    assert rectangle.left == -8
    assert rectangle.bottom == -4
    assert rectangle.right == -5
    assert rectangle.width == 3
    assert rectangle.height == 3
    assert rectangle.topleft == Point(-8, -1)
    assert rectangle.bottomleft == Point(-8, -4)
    assert rectangle.topright == Point(-5, -1)
    assert rectangle.bottomright == Point(-5, -4)
    assert rectangle.center == Point(-6.5, -2.5)

def test_attributesC():
    rectangle = Rectangle(-3, -2, 3, 2)
    assert rectangle.top == 2
    assert rectangle.left == -3
    assert rectangle.bottom == -2
    assert rectangle.right == 3
    assert rectangle.width == 6
    assert rectangle.height == 4
    assert rectangle.topleft == Point(-3, 2)
    assert rectangle.bottomleft == Point(-3, -2)
    assert rectangle.topright == Point(3, 2)
    assert rectangle.bottomright == Point(3, -2)
    assert rectangle.center == Point(0, 0)

if __name__ == "__main__":
    pytest.main()
