import unittest
from main import count_occurence


seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'


class TestINI(unittest.TestCase):
    def test_count_occurence(self):
        self.assertEqual(count_occurence(seq, 'A'), 20)
        self.assertEqual(count_occurence(seq, 'C'), 12)
        self.assertEqual(count_occurence(seq, 'G'), 17)
        self.assertEqual(count_occurence(seq, 'T'), 21)


if __name__ == '__main__':
    unittest.main()

