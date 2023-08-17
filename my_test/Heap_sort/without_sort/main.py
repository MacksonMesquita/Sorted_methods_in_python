#without sort
 
def heapify(arr, n, i):
      largest = i # defininfo o pai 
      l = 2 * i + 1 # fazendo a divisão dos filhos
      r = 2 * i + 2 # fazendo a divisão dos filhos
  
      if l < n and arr[i] < arr[l]:
          largest = l  
      if r < n and arr[largest] < arr[r]:
          largest = r

      # setando as posições do maior para o menor de acordo com o filho
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
def heapSort(arr):
      n = len(arr)
      for i in range(n//2, -1, -1):# setando o heap maximo 
          heapify(arr, n, i)

          #trocando de root
      for i in range(n-1, 0, -1):
          arr[i], arr[0] = arr[0], arr[i]
          heapify(arr, i, 0)
      return arr
                   
           
numbers = [2, 5, 7, 9, 1, 4, 10, 42]
heapSort(numbers)
