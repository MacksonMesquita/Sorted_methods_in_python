#without sort

arr = [1, 5, 3, 7, 9, 6, 2, 20, 54, 11]

def mergesort(arr):
 if len(arr) > 1:
    rigth = len(arr)//2 # define o ponto em que o corte acontece
    left = arr[:rigth] # define o lado direito do subarray
    mid = arr[rigth:]  # define o lado esquerdo do subarray
    
    mergesort(left)
    mergesort(mid)
    i = 0
    j = 0
    k =0 
    # definindo o ponto inicial de cada variavel

    while i < len(left) and j < len(mid):
        if left[i] < mid[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = mid[j]
            j += 1
        k += 1
        # percorrendo as duas listas divididas separando-as

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(mid):
        arr[k] = mid[j]
        j += 1
        k += 1
        #acrescentando os elementos de volta a lista, todavia de forma ordenada
    return arr
 print(arr)