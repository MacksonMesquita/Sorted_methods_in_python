#with sort

from pprint import pprint

produtos = [
    {"produtos": 'laranja', "id": 5 },
    {"produtos": 'berinjela', "id": 3 },
    {"produtos": 'pitaia', "id": 1 },
    {"produtos": 'tomate', "id": 4  },
    {"produtos": 'carambola', "id": 2 },
]

produtos.sort(key=lambda elements:elements["id"])
pprint(produtos)