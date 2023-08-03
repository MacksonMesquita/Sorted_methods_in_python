#with sort

import unittest
from main import produtos 


class TestProdutos2(unittest.TestCase):    
    
    def test_is_working(self):
        resultado2 = [
            {"produtos": 'pitaia', "id": 1 },
            {"produtos": 'carambola', "id": 2 },
            {"produtos": 'berinjela', "id": 3 },
            {"produtos": 'tomate', "id": 4 },
            {"produtos": 'laranja', "id": 5 },    
        ]
        self.assertEqual(produtos, resultado2) 


if __name__ == '__main__':
    unittest.main()