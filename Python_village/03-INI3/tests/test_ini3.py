import unittest
from main import string_slice, string_slice_lc

class TestSliceOfString(unittest.TestCase):
    def test_string_slice(self):
        self.assertEqual(string_slice(
            'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.',
            22, 27), 'Humpty')
        self.assertEqual(string_slice(
            'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.',
            97, 102), 'Dumpty')
    def test_string_slice_list_comprehension(self):
        self.assertEqual(string_slice_lc(
            'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.',
            22, 27), 'Humpty')
        self.assertEqual(string_slice_lc(
            'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.',
            97, 102), 'Dumpty')
