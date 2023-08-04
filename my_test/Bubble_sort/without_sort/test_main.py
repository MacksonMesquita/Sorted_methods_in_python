#without sort

import unittest
from main import numbers

class TestProdutos(unittest.TestCase):

    def test_is_working(self):
        resultado = [1, 2, 3, 4, 5, 7, 9, 10, 12, 20, 21, 34, 66, 67, 69, 77, 88, 89, 99, 100]
        self.assertEqual(numbers, resultado)


if __name__ == '__main__':
    unittest.main()