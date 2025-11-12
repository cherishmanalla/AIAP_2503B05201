import unittest

from task5 import sum_of_odd_numbers, sum_of_even_numbers, sum_odd_and_even


class TestOddEvenSums(unittest.TestCase):
    def test_sum_of_odd_numbers_basic(self):
        self.assertEqual(sum_of_odd_numbers([1, 2, 3, 4, 5]), 9)

    def test_sum_of_odd_numbers_no_odds(self):
        self.assertEqual(sum_of_odd_numbers([2, 4, 6]), 0)

    def test_sum_of_odd_numbers_all_odds(self):
        self.assertEqual(sum_of_odd_numbers([1, 3, 5, 7]), 16)

    def test_sum_of_odd_numbers_negative(self):
        self.assertEqual(sum_of_odd_numbers([-1, -2, -3, 4]), -4)

    def test_sum_of_odd_numbers_empty(self):
        self.assertEqual(sum_of_odd_numbers([]), 0)

    def test_sum_of_even_numbers_basic(self):
        self.assertEqual(sum_of_even_numbers([1, 2, 3, 4, 5]), 6)

    def test_sum_of_even_numbers_no_evens(self):
        self.assertEqual(sum_of_even_numbers([1, 3, 5]), 0)

    def test_sum_of_even_numbers_all_evens(self):
        self.assertEqual(sum_of_even_numbers([2, 4, 6, 8]), 20)

    def test_sum_of_even_numbers_negative(self):
        self.assertEqual(sum_of_even_numbers([-2, -4, 3, 5]), -6)

    def test_sum_of_even_numbers_empty(self):
        self.assertEqual(sum_of_even_numbers([]), 0)

    def test_sum_odd_and_even_basic(self):
        self.assertEqual(sum_odd_and_even([1, 2, 3, 4, 5]), (9, 6))

    def test_sum_odd_and_even_zero(self):
        self.assertEqual(sum_odd_and_even([0]), (0, 0))

    def test_sum_odd_and_even_mixed_negative(self):
        self.assertEqual(sum_odd_and_even([-1, -2, 3, 4]), (2, 2))

    def test_sum_odd_and_even_empty(self):
        self.assertEqual(sum_odd_and_even([]), (0, 0))


if __name__ == '__main__':
    unittest.main()
