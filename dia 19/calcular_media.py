# nesse dia, vou criar uma função que clacula a média de uma lista de números

def calcula_media(numeros : list):

    try:

        resultado = sum(numeros) / len(numeros)
        resultado = round(resultado)

        return resultado
    
    except Exception as erro:
        print('erro encontrado: ')

print(calcula_media([10, 47, 5, 556, 99, 67]))
