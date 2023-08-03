#without sort

numbers = [
   5,3,2,1,9,7,10,34,67,99,88,
   77,66,89,100,20,21,69,12,4]

for x in range(len(numbers)-1): # pela length de produtos -1 produto atual (by length of products -1 current product)
    for y in range(len(numbers)-x-1):
      if numbers[y] > numbers[y+1]: 
        temp = numbers[y]
        numbers[y] = numbers[y+1]#
        numbers[y+1] = temp
    print(numbers)

#bubble sort method
      
