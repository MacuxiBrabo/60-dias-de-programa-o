# nesse arquivo vou criar uma função que fator um número

def fatorial(numero):
    try:

        if numero < 0:
            raise ValueError('o número precisa ser positivo(maior que zero)')

        if numero == 0 or numero == 1:
            return 1

        resultado = 1

        while numero != 1:
            print(numero)
            resultado = resultado * numero
            numero = numero - 1

        return resultado

    except Exception as erro:
        print('erro encontrado:', erro)

numero = fatorial(5)
print(numero)