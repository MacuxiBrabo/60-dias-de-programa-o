# nesse arquivo vou criar uma função que faz uma busca linear em uma lista de números

def busca_linear(lista, numero_procurado):

    try:

        for indice, numero in enumerate(lista, start = 1):

            if numero == numero_procurado:
                print(f'número encontrado: indice: {indice}, número: {numero}')
                return None

        print('número não encontrado')

    except Exception as erro:
        print('erro encontrado: ', erro)

    return None

lista = [556, 762, 2, 3, 5, 7]

busca_linear(lista, 10)
