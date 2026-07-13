entrada = input('coloque um número inteiro para análise -> ')

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print('esse número é par')

    else:
        print('esse número é impar')

except ValueError as erro:
    print('é necessário o número ser inteiro para a análise')