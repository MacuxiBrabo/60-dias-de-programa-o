# nesse arquivo vou criar um contador que começa de até o numero que o usúario digitar

def contador():

    try:
        limite = int(input('qual será o limite do contador -> '))

        pergunta = limite < 0

        if pergunta:
            print('o limite precisa ser maior que 0')
            contador()

        for numero in range(1, limite + 1):
            print(numero)

    except ValueError as erro:
        print('Valor incorreto, insira um número inteiro')
        contador()

    return None

contador()