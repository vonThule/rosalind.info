import unittest
from main import hypotenuse_square

class TestSquareOfHypotenuse(unittest.TestCase):
    def test_square(self):
        self.assertEqual(hypotenuse_square(3, 5), 34)
