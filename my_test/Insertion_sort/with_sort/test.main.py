#with sort

import unittest
from main import insertionsort

class TestNumbers(unittest.TestCase):

    def test_is_working(self):
        esperado = [1, 2, 3, 5, 6, 7, 9] 
        arr = [1, 5, 3, 7, 9, 6, 2] 
        resultado = insertionsort(arr)
        self.assertEquals(resultado, esperado)


if __name__ == '__main__':
    unittest.main()