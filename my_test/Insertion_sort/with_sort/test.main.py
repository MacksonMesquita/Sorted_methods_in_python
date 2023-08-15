#with sort

import unittest
from main import numbers

class TestNumbers(unittest.TestCase):

    def test_is_working(self):
        resultado = [1, 2, 3, 5, 6, 7, 9]
        self.assertEqual(numbers, resultado)


if __name__ == '__main__':
    unittest.main()