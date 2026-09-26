# nesse dia, vou criar uma calculadora de imc(índice de massa corporal)

def calcular_imc():
    try:

        peso = float(input('Digite seu peso em kg(quilogramas): '))
        altura = float(input('Digite sua altura em metros: '))

        if altura <= 0 or peso <= 0:
            ValueError('Peso ou altura incorretos')

        imc = round(peso / (altura ** 2), 1)

        if imc < 18.5:
            print('Abaixo do peso ideal')
        elif imc >= 18.5 or imc <= 24.9:
            print('peso ideal')
        elif imc >= 25.0 or imc <= 29.9:
            print('Sobrepeso')
        elif imc >= 30.0 or imc <= 34.9:
            print('Obesidade grau I')
        elif imc >= 35.0 or imc <= 39.9:
            print('Obesidade grau II')
        else:
            print('Obesidade grau III')

    except Exception as erro:
        print('Erro encontrado: ', erro)

if __name__ == '__main__':
    calcular_imc()