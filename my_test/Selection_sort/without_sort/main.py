#without sort

def selectionsort(numbers):
 numbers = [9, 20, 1, 6, 8, 11]

 for step in range(len(numbers)): 
        min_idx = step
        
        for i in range(step+1, len(numbers)): 
            if numbers[min_idx] > numbers[i]:
                min_idx = i
        numbers[step], numbers[min_idx] = numbers[min_idx], numbers[step]

 return numbers 
