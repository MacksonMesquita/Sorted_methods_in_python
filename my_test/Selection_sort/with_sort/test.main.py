#with sort

import unittest
from main import numbers

class TestNumbers(unittest.TestCase):

    def test_is_working(self):
        resultado = [1, 6, 8, 9, 11, 20] 
        self.assertEqual(numbers, resultado)


if __name__ == '__main__':
    unittest.main()