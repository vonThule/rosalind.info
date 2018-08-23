import unittest
from main import sum_of_odd

class TestSumOfAllOddIntegers(unittest.TestCase):
    def test_sum_of_odd(self):
        self.assertEqual(sum_of_odd(100, 200), 7500)
