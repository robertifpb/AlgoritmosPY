numeros = []
for i in range(15):
    num = int (input(f"Digite o {i+1}° número: "))
    numeros.append(num)

print("\n Lista de números digitados: ", numeros)   

maior = max(numeros)
menor = min(numeros)
pos_maior =  numeros.index(maior) + 1
pos_menor =  numeros.index(menor) + 1

print("\f Maior Valor: {maior}, na posição (maior)")
print("\f Menor Valor:{menor}, na posição (menor)")