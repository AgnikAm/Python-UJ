import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(10), 3628800)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)

    def test_odwracanie(self):
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        odwracanie(list1, 0, 9)
        self.assertEqual(list1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        odwracanie(list1, -10, 9)
        self.assertEqual(list1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        odwracanie(list1, 0, 100)
        self.assertEqual(list1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        odwracanie(list1, 3, 7)
        self.assertEqual(list1, [9, 8, 7, 2, 3, 4, 5, 6, 1, 0])

        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        rec_odwracanie(list1, 0, 9)
        self.assertEqual(list1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        rec_odwracanie(list1, -10, 9)
        self.assertEqual(list1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        rec_odwracanie(list1, 0, 100)
        self.assertEqual(list1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        rec_odwracanie(list1, 3, 7)
        self.assertEqual(list1, [9, 8, 7, 2, 3, 4, 5, 6, 1, 0])

        list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        odwracanie(list2, 0, 6)
        self.assertEqual(list2, ['g', 'f', 'e', 'd', 'c', 'b', 'a'])
        odwracanie(list2, -10, 6)
        self.assertEqual(list2, ['g', 'f', 'e', 'd', 'c', 'b', 'a'])
        odwracanie(list2, 0, 100)
        self.assertEqual(list2, ['g', 'f', 'e', 'd', 'c', 'b', 'a'])
        odwracanie(list2, 4, 6)
        self.assertEqual(list2, ['g', 'f', 'e', 'd', 'a', 'b', 'c'])

        list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        rec_odwracanie(list2, 0, 6)
        self.assertEqual(list2, ['g', 'f', 'e', 'd', 'c', 'b', 'a'])
        rec_odwracanie(list2, -10, 6)
        self.assertEqual(list2, ['g', 'f', 'e', 'd', 'c', 'b', 'a'])
        rec_odwracanie(list2, 0, 100)
        self.assertEqual(list2, ['g', 'f', 'e', 'd', 'c', 'b', 'a'])
        rec_odwracanie(list2, 4, 6)
        self.assertEqual(list2, ['g', 'f', 'e', 'd', 'a', 'b', 'c'])

    def test_sum_seq(self):
        self.assertEqual(sum_seq([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(sum_seq([1, (2, 3), 3, 4]), [1, 5, 3, 4])
        self.assertEqual(sum_seq([[], (2, 3), 3, [4, 5, 6]]), [0, 5, 3, 15])
        self.assertEqual(sum_seq([1,(2,3),[],[4,(5,6,7)],8,[9]]), [1, 5, 0, 22, 8, 9])

    def test_flatten(self):
        self.assertEqual(flatten([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(flatten([1, (2, 3), 3, 4]), [1, 2, 3, 3, 4])
        self.assertEqual(flatten([[], (2, 3), 3, [4, 5, 6]]), [2, 3, 3, 4, 5, 6])
        self.assertEqual(flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(flatten([8, (2, 9), [], [1, (3, 2, 3)], 0, [9]]), [8, 2, 9, 1, 3, 2, 3, 0, 9])

if __name__ == '__main__':
    unittest.main()