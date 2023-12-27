import unittest
from unittest import mock
import sys
from io import StringIO
from functions import *

class TestFunctions(unittest.TestCase):

    def test_not_divisible_by_3(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        not_divisible_by_3()

        sys.stdout = sys.__stdout__
        
        expected_output = "1\n2\n4\n5\n7\n8\n10\n11\n13\n14\n16\n17\n19\n20\n22\n23\n25\n26\n28\n29"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    @mock.patch('builtins.input', side_effect=['4', 'stop'])
    def test_third_pow_numerical(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output

        third_pow()

        sys.stdout = sys.__stdout__

        expected_output = "4^3 is 64"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    @mock.patch('builtins.input', side_effect=['some string', 'stop'])
    def test_third_pow_string(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output

        third_pow()

        sys.stdout = sys.__stdout__

        expected_output = "Wrong input. Please enter a number or 'stop'"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_ruler(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        ruler(12)

        sys.stdout = sys.__stdout__
        expected_output = "|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11   12"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_duplicated_elements(self):
        a = [0, 3, 6, 9]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(duplicated_elements(a, b), [3, 6, 9])
    
    def test_common_elements(self):
        a = [0, 3, 6, 9]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(common_elements(a, b), [0, 3, 6, 9, 1, 2, 4, 5, 7, 8])
    
    def test_sum_sequence(self):
        seq = [[],[4],(1,2),[3,4],(5,6,7)]
        self.assertEqual(sum_sequence(seq), [0,4,3,7,18])

    def test_roman2int(self):
        self.assertEqual(roman2int("VIII"), 8)
        self.assertEqual(roman2int("CXCIX"), 199)
        self.assertEqual(roman2int("CCCLIV"), 354)
        self.assertEqual(roman2int("MMMDCCXXIV"), 3724)


if __name__ == '__main__':
    unittest.main()