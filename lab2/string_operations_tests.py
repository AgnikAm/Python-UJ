import unittest
from string_operations import *

class TestString(unittest.TestCase):
    text1 = "This is a test"
    text2 = """
            This is a multi-line
            test
            """
    def test_count_words(self):
        self.assertEqual(count_words(self.text1), 4)
        self.assertEqual(count_words(self.text2), 5)

    def test_underscore(self):
        word1 = "hello"
        word2 = """
                world
                """
        self.assertEqual(underscore(word1), "h_e_l_l_o")
        self.assertEqual(underscore(word2.strip()), "w_o_r_l_d")

    def test_first_letter_word(self):
        self.assertEqual(first_letter_word(self.text1), "Tiat")
        self.assertEqual(first_letter_word(self.text2), "Tiamt")

    def test_last_letter_word(self):
        self.assertEqual(last_letter_word(self.text1), "ssat")
        self.assertEqual(last_letter_word(self.text2), "ssaet")

    def test_len_of_words(self):
        self.assertEqual(len_of_words(self.text1), 11)
        self.assertEqual(len_of_words(self.text2), 21)

    def test_longest_word(self):
        self.assertEqual(longest_word(self.text1), "This")
        self.assertEqual(longest_word(self.text2), "multi-line")

    def test_gvr(self):
        self.assertEqual(gvr("GvR is BDFL"), "Guido van Rossum is BDFL")
        self.assertEqual(gvr("GvR\n is BDFL"), "Guido van Rossum\n is BDFL")
        self.assertEqual(gvr("GvRis\n BDFL"), "Guido van Rossumis\n BDFL")

    def test_alpha_sort(self):
        self.assertEqual(alpha_sort("alfa gamma delta beta"), ["alfa", "beta", "delta", "gamma"])
        self.assertEqual(alpha_sort("""alfa gamma 
                                    delta beta"""), ["alfa", "beta", "delta", "gamma"])

    def test_len_sort(self):
        self.assertEqual(len_sort("One Two Three Four"), ["One", "Two", "Four", "Three"])
        self.assertEqual(len_sort("""One Two 
                                    Three Four"""), ["One", "Two", "Four", "Three"])


if __name__ == '__main__':
    unittest.main()
