import unittest
from fracs import *

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-3, 4], [-1, 4]), [-16, 16])
        self.assertEqual(add_frac([0, 2], [1, 3]), [2, 6])
        with self.assertRaises(ValueError):
            add_frac([1, 0], [1, 3])
            add_frac([1, 2], [1, 0])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([-3, 4], [-1, 4]), [-8, 16])
        self.assertEqual(sub_frac([0, 2], [1, 3]), [-2, 6])
        with self.assertRaises(ValueError):
            sub_frac([1, 0], [1, 3])
            sub_frac([1, 2], [1, 0])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([-3, 4], [-1, 4]), [3, 16])
        self.assertEqual(mul_frac([0, 2], [1, 3]), [0, 6])
        self.assertEqual(mul_frac([1, 4], [-1, 4]), [-1, 16])
        with self.assertRaises(ValueError):
            mul_frac([1, 0], [1, 3])
            mul_frac([1, 2], [1, 0])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([-3, 4], [-1, 4]), [-12, -4])
        self.assertEqual(div_frac([0, 2], [1, 3]), [0, 2])
        self.assertEqual(div_frac([1, 4], [-1, 4]), [4, -4])
        with self.assertRaises(ValueError):
            div_frac([1, 0], [1, 3])
            div_frac([1, 2], [1, 0])
            div_frac([1, 2], [0, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-3, 4]), False)
        self.assertEqual(is_positive([0, 2]), "The number is zero")
        self.assertEqual(is_positive([1, -4]), False)
        with self.assertRaises(ValueError):
            is_positive([1, 0])

    def test_is_zero(self):
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([-3, 4]), False)
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([1, -4]), False)
        with self.assertRaises(ValueError):
            is_zero([1, 0])

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([-1, 2], [1, -2]), 0)
        self.assertEqual(cmp_frac([0, 1], [0, 2]), 0)
        self.assertEqual(cmp_frac([3, 1], [6, 2]), 0)
        self.assertEqual(cmp_frac([-3, 4], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [3, -4]), 1)
        with self.assertRaises(ValueError):
            cmp_frac([1, 0], [1, 3])
            cmp_frac([1, 2], [1, 0])

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([-3, 4]), -0.75)
        self.assertEqual(frac2float([0, 2]), 0)
        self.assertEqual(frac2float([1, -4]), -0.25)
        with self.assertRaises(ValueError):
            frac2float([1, 0])


if __name__ == '__main__':
    unittest.main()
