# nesse dia, vou criar um gerador de números aleatórias
import random

def gerador_numeros_aleatorios():
    try:
        print('gerador de números aleatórios')

        numeros_aleatorios = [random.randint(1, 100) for numero in range(10)]

        print('\nnúmeros sorteados: ')
        
        for contador, numero in enumerate(numeros_aleatorios, start = 1): 
            print(f'números {contador}: {numero}')

    
    except Exception as erro:
        print('Erro encontrado: ', erro)

if __name__ == '__main__':
    gerador_numeros_aleatorios()