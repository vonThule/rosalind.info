import unittest
from main import get_processes


class TestDBPR(unittest.TestCase):
    def test_get_processes(self):
        self.assertEqual(get_processes('Q5SLP9'), ['DNA recombination', 'DNA repair', 'DNA replication'])


if __name__ == '__main__':
    unittest.main()

