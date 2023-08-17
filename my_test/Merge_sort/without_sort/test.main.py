#without sort

import unittest
from main import mergesort

class Testnumbers(unittest.TestCase):

    def test_is_working(self):
        esperado = [1, 2, 3, 4, 5, 7, 9, 10, 12, 20, 21, 34, 66, 67, 69, 77, 88, 89, 99, 100]
        arr = [5, 3, 2, 1, 9, 7, 10, 34, 67, 99, 88, 77, 66, 89, 100, 20, 21, 69, 12, 4]
        resultado = mergesort(arr)
        self.assertEquals(resultado, esperado)


if __name__ == '__main__':
    unittest.main(verbosity=2)