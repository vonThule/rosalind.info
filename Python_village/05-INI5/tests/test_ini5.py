import unittest
from main import get_even_number_lines


lines_to_read = ["Bravely bold Sir Robin rode forth from Camelot",
                 "Yes, brave Sir Robin turned about",
                 "He was not afraid to die, O brave Sir Robin",
                 "And gallantly he chickened out",
                 "He was not at all afraid to be killed in nasty ways",
                 "Bravely talking to his feet",
                 "Brave, brave, brave, brave Sir Robin",
                 "He beat a very brave retreat"]
lines_to_output = ["Yes, brave Sir Robin turned about",
                   "And gallantly he chickened out",
                   "Bravely talking to his feet",
                   "He beat a very brave retreat"]


class TestGetEvenNumberLines(unittest.TestCase):
    def test_get_even_number_lines(self):
        self.assertEqual(get_even_number_lines(lines_to_read), lines_to_output)

