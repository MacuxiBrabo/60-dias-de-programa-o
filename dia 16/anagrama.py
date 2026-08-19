# nesse dia, vou criar um programa que verifica se uma palavra é um anagrama

def verificador_anagrama(palavra1 , palavra2):

    '''
    essa função verifica se as duas palavra colocadas como parametro
    são anagrama, ou seja, utilizam as mesmas letras para formar palavras
    diferêntes

    o retorno da função será um booleano, True: é anagrama, False: não é 
    anagrama

    palavra1 é a primeira palavra
    palavra2 é a segunda palavra
    '''

    try:

        palavra1 = sorted(palavra1.replace(' ', '').lower())
        palavra2 = sorted(palavra2.replace(' ', '').lower())

        resultado = palavra1 == palavra2

        return resultado
    
    except Exception as erro:
        print('erro encontrado:', erro)

print(verificador_anagrama('rota', 'rato'))