#with sort

from pprint import pprint

numbers = [9, 20, 1, 6, 8, 11]

numbers.sort(key=lambda elements:elements)
pprint(numbers)