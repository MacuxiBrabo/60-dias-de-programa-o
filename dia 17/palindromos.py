# nesse dia, vou aprender a manipular string e criar um programa que identifica palindromos

def verifica_palindromo(texto):
    try:

        texto = str(texto).replace(' ', '').lower()

        resultado = texto == texto[::-1]

        if resultado:
            return f'{texto} é um palíndromo'
        return f'{texto} não é um palíndromo'
    
    except Exception as erro:
        print('erro encontrado:', erro)

print(verifica_palindromo('A grama e amarga'))