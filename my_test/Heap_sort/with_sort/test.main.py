#with sort

import unittest
from main import heapsort

class Testnumbers(unittest.TestCase):

    def test_is_working(self):
        esperado = [1, 2, 4, 5, 7, 9, 10, 42]
        arr = [2, 5, 7, 9, 1, 4, 10, 42]
        resultado = heapsort(arr)
        self.assertEquals(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
