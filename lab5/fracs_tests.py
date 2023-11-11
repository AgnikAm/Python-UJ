import unittest

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-3, 4], [-1, 4]), [-4, 4])
        self.assertEqual(add_frac([0, 2], [1, 3]), [2, 6])
        self.assertEqual(add_frac([1, 0], [1, 3]), "Wrong input. Each fraction should be a list of two numbers: nominator and denominator")

    def test_sub_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(add_frac([-3, 4], [-1, 4]), [-2, 4])
        self.assertEqual(add_frac([0, 2], [1, 3]), [-2, 6])
        self.assertEqual(add_frac([1, 0], [1, 3]), "Wrong input. Each fraction should be a list of two numbers: nominator and denominator")

    def test_mul_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(add_frac([-3, 4], [-1, 4]), [3, 16])
        self.assertEqual(add_frac([0, 2], [1, 3]), [0, 6])
        self.assertEqual(add_frac([1, 4], [-1, 4]), [-1, 16])
        self.assertEqual(add_frac([1, 0], [1, 3]), "Wrong input. Each fraction should be a list of two numbers: nominator and denominator")

    def test_div_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(add_frac([-3, 4], [-1, 4]), [-12, -4])
        self.assertEqual(add_frac([0, 2], [1, 3]), [0, 1])
        self.assertEqual(add_frac([1, 4], [-1, 4]), [4, -4])
        self.assertEqual(add_frac([1, 0], [1, 3]), "Wrong input. Each fraction should be a list of two numbers: nominator and denominator")

    def test_is_positive(self):
        self.assertEqual(add_frac([1, 2]), True)
        self.assertEqual(add_frac([-3, 4]), False)
        self.assertEqual(add_frac([0, 2]), "The number is zero")
        self.assertEqual(add_frac([1, -4]), False)
        self.assertEqual(add_frac([1, 0], [1, 3]), "Wrong input. Each fraction should be a list of two numbers: nominator and denominator")

    def test_is_zero(self):
        self.assertEqual(add_frac([1, 2]), False)
        self.assertEqual(add_frac([-3, 4]), False)
        self.assertEqual(add_frac([0, 2]), True)
        self.assertEqual(add_frac([1, -4]), False)
        self.assertEqual(add_frac([1, 0], [1, 3]), "Wrong input. Each fraction should be a list of two numbers: nominator and denominator")

    def test_cmp_frac(self): pass

    def test_frac2float(self):
        self.assertEqual(add_frac([1, 2]), 0.5)
        self.assertEqual(add_frac([-3, 4]), -0.75)
        self.assertEqual(add_frac([0, 2]), 0)
        self.assertEqual(add_frac([1, -4]), -0.25)
        self.assertEqual(add_frac([1, 0], [1, 3]), "Wrong input. Each fraction should be a list of two numbers: nominator and denominator")


if __name__ == '__main__':
    unittest.main()
