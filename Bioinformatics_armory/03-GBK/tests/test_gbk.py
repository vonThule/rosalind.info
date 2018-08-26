import unittest
from main import get_number_entries


class TestGBK(unittest.TestCase):
    def test_get_number_entries(self):
        self.assertEqual(get_number_entries('test@test.com', 'Anthoxanthum', '2003/07/25', '2005/12/27'), 7)


if __name__ == '__main__':
    unittest.main()

