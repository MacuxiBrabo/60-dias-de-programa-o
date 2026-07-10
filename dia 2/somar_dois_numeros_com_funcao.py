def somar_dois_numeros(numero_1 : int, numero_2 : int):
    soma = numero_1 + numero_2
    print(f'a soma dos dois números são {soma}')
    return soma

#print(somar_dois_numeros(8000, 5000))

def pedir_dois_numeros():
    numero_1 = int(input('digite o primeiro número -> '))
    numero_2 = int(input('digite o segundo número -> '))

    somar_dois_numeros(numero_1, numero_2)

pedir_dois_numeros()