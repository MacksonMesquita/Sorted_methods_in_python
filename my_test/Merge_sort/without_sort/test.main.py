#without sort

import unittest
from main import mergesort

class TestNumbers(unittest.TestCase):

    def test_is_working(self):
        esperado = [1, 2, 3, 5, 6, 7, 9, 11, 20, 54] 
        arr = [1, 5, 3, 7, 9, 6, 2, 20, 54, 11] 
        resultado = mergesort(arr)
        self.assertEquals(resultado, esperado)


if __name__ == '__main__':
    unittest.main()