from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 < x2 and y1 < y2:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else: raise ValueError("Wrong coordinates. x1 must be smaller than x2 and y1 must be smaller than y2")

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("Two points are required to create a rectangle. lower left and upper right")

        x1, y1 = points[0].x, points[0].y
        x2, y2 = points[1].x, points[1].y

        return cls(x1, y1, x2, y2)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)



