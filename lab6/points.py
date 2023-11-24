class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self.x, self.y

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self.x, self.y

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x**2 + self.y**2)**(1/2)

    def __hash__(self):
        return hash((self.x, self.y)) # bazujemy na tuple, immutable points