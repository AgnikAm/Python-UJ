import unittest
from nums_operations import *

class TestNums(unittest.TestCase):
    num1 = 9
    num2 = 70
    num3 = 400
    L = [num1, num2, num3]

    def test_create_string(self):
        self.assertEqual(create_string(self.L), "970400")

    def test_count_zeros(self):
        self.assertEqual(count_zeros(self.num1), 0)
        self.assertEqual(count_zeros(self.num2), 1)
        self.assertEqual(count_zeros(self.num3), 2)

    def test_transform(self):
        self.assertEqual(transform(self.num1), "009")
        self.assertEqual(transform(self.num2), "070")
        self.assertEqual(transform(self.num3), "400")

if __name__ == '__main__':
    unittest.main()