numeros = []
soma = 0
quantidade = 0
opcao = 1
while(opcao !=0):
    num = int(input('Digite um número: '))
    numeros.append(num)
    soma = soma + num
    quantidade = quantidade + 1
    opcao = int(input('0 (sair) - 1 (novo número): '))
print(f'Soma {soma} - Média: {soma/quantidade}')
