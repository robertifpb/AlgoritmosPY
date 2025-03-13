numeros = [1,2,3,4,5,6,7,8,9,10]
primeiro = numeros[0]
for i in range(len(numeros) - 1):
    numeros[i] = numeros[i+1]
numeros[-1] = primeiro
print("Lista modificada:", numeros)
