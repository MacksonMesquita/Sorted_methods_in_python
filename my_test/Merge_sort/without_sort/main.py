#without sort

def mergesort(content):    
    if len(content) > 1:

        step = len(content)//2 #ponto onde o content será dividido em dois sub arrays
        L = content[:step] # chmando a primeira metade 
        M = content[step:] # chamando a segunda metade 

        mergesort(L)
        mergesort(M)
        i = j = k = 0
        # sorteando as duas metades 

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                content[k] = L[i]
                i += 1
            else:
                content[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            content[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            content[k] = M[j]
            j += 1
            k += 1
            return content 
        # percorrendo a len de cada metade respectiva, e setando as divisões que ocorreram em cada caso 

arr_exmaple = [5, 3, 2, 1, 9, 7, 10, 34, 67, 99, 88, 77, 66, 89, 100, 20, 21, 69, 12, 4]
mergesort(arr_exmaple)

