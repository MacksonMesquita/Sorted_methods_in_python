#without sort

numbers = [1,5,3,7,9,6,2] 
 
for i in range(1, len(numbers)): #de 1 em 1 até o final da len de numbers
    key = numbers[i]# guardando o primeiro valor 
    j = i-1 # passando para o prox number
    while j >= 0 and key < numbers[j]: # enquanto o o proximo valor menor ou igual a 0, e a key anterior (numero anterior), adiciona tal numero
            numbers[j + 1] = numbers[j]
            j = j - 1 # prox numero menos
    numbers[j + 1] = key
    print(numbers)

 