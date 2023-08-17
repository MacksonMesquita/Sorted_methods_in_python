#with sort

def mergesort(numbers):
 numbers =[5, 3, 2, 1, 9, 7, 10, 34, 67, 99, 88, 77, 66, 89, 100, 20, 21, 69, 12, 4]

 numbers.sort(key=lambda elements:elements)
 return numbers