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

    def center(self):
        center_point = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        return center_point

    def area(self):
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        rectangle = Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)
        return rectangle

    def intersection(self, other):
        x_start = max(self.pt1.x, other.pt1.x)
        y_start = max(self.pt1.y, other.pt1.y)
        x_end = min(self.pt2.x, other.pt2.x)
        y_end = min(self.pt2.y, other.pt2.y)

        if x_start < x_end and y_start < y_end:
            intersection_rectangle = Rectangle(x_start, y_start, x_end, y_end)
            return intersection_rectangle
        else:
            return None

    def cover(self, other):
        x_start = min(self.pt1.x, other.pt1.x)
        y_start = min(self.pt1.y, other.pt1.y)
        x_end = max(self.pt2.x, other.pt2.x)
        y_end = max(self.pt2.y, other.pt2.y)

        if x_start < x_end and y_start < y_end:
            intersection_rectangle = Rectangle(x_start, y_start, x_end, y_end)
            return intersection_rectangle
        else:
            return None

    def make4(self):
        rect1 = Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y) # lower left
        rect2 = Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y) # upper left
        rect3 = Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y) #upper right
        rect4 = Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y) #lower right

        return rect1, rect2, rect3, rect4



