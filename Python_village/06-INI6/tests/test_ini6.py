import unittest
from main import count_occurrences


string = ["We", "tried", "list", "and", "we", "tried", "dicts", "also", "we", "tried", "Zen"]
result = {"and": 1, "We": 1, "tried": 3, "dicts": 1, "list": 1, "we": 2, "also": 1, "Zen": 1}

class TestCountWordOccurrence(unittest.TestCase):
    def test_count_occurrences(self):
        self.assertEqual(count_occurrences(string), result)
