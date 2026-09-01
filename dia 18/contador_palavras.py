# nesse dia, vou fazer um contador de palavras

def contador_palavras(palavra):
    '''
    param palavra: recebe a palavra que vai ser contada

    '''

    resultado = len(palavra.split())

    return resultado

print(contador_palavras('procuro o cálice sagrado'))