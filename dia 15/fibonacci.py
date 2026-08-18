# nesse dia, vou codificar a seguencia de fibonacci

try:
    fibonacci = [0, 1]
    limite = 8

    for contador in range(limite):
        proximo_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_numero)

    print('limite da seguência:', limite)
    print(fibonacci)

except Exception as erro:
    print('erro encontrado:', erro)
