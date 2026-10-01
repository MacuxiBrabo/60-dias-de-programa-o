# nesse dia, vou fazer um jogo de adivinhação

import random

def jogo_adivinhacao():
    try:
        print('=' * 30)
        print('Bem-vindo ao jogo de adivinhação!!!')
        print('=' * 30)

        numero_sorteado = random.randint(0, 20)

        tentativas = 0

        while True:
            palpite = int(input('palpite: '))

            if palpite > numero_sorteado:
                print('mais baixo')
                tentativas += 1
                
            elif palpite < numero_sorteado:
                print('mais alto')
                tentativas += 1

            elif palpite == numero_sorteado:
                print('você acertou')
                tentativas += 1
                break

        print(f'o número correto é {numero_sorteado}, suas tentativas: {tentativas}')

    except Exception as erro:
        print('erro encontrado: ', erro)

if __name__ == '__main__':
    jogo_adivinhacao()