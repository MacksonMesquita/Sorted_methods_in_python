#with sort

import unittest
from main import selectionsort

class TestNumbers(unittest.TestCase):

    def test_is_working(self):
        esperado = [1, 6, 8, 9, 11, 20]
        arr = [9, 20, 1, 6, 8, 11]
        resultado = selectionsort(arr)
        self.assertEquals(resultado, esperado)


if __name__ == '__main__':
    unittest.main()