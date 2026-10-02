# nesse diam, vou criar um programa que mostra a tabuada que o usúario quiser

def tabuad():
    try:

        fator_1 = int(input('Digite o número deseja ter a tabuada: '))

        print(f'\ntabuada do {fator_1}')

        for fator_2 in range(1, 11):
            produto = fator_1 * fator_2
            print(f'{fator_1} x {fator_2} = {produto}')

    except Exception as erro:
        print('erro encontrado: ', erro)

if __name__ == '__main__':
    tabuad()