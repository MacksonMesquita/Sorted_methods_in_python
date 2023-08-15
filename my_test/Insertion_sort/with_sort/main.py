#with sort

from pprint import pprint

numbers = [1,5,3,7,9,6,2] 

numbers.sort(key=lambda elements:elements)
pprint(numbers)