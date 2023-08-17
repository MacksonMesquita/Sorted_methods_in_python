#with sort

def heapsort(numbers):
    numbers = [2, 5, 7, 9, 1, 4, 10, 42]

    numbers.sort(key=lambda elements:elements)
    return numbers
