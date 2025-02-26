def decimal_para_hexadecimal(decimal):
    return hex(decimal)

numero_decimal = int(input("Digite um número decimal: "))
numero_hexadecimal = decimal_para_hexadecimal(numero_decimal)

print(f"O número {numero_decimal} em hexadecimal é {numero_hexadecimal[2:]}")