# nesse dia vou criar uma função que faz uma matrix transposta

def transpor_matrix(matrix):
    '''
    matrix é um conjunto de números, distribuidos em colunas(vertical) e linhas(horizontal)
    nessa função, uma matrix 3x3 que vai transpostar a linha em uma coluna

    exemplo:

    [2, 3, 5]                [2, 2, 2]
    [2, 3, 5]     ----->     [3, 3, 3]
    [2, 3, 5]                [5, 5, 5]

    parametro: matrix é a matrix que será transporta
    returno: a matrix transportada como no exemplo
    '''

    try:

        transposta = [[matrix[numero][linha] for numero in range(3)] for linha in range(3)]
        '''
        o que está acontacendo?

        o 'for linha in range(3)' percorre por todas as linhas da matrix e 
        cria cada linha de forma automática

        o 'for numero in range(3)' percorre por cada um dos números da linha
        para resulta no mesmo número
        
        o 'matrix[numero][linha]' é o segredo, porque o código não copia o 
        primeiro número de linha e cola nela toda, ele pega a posição da 
        linha para identificar o número e pega a posição do número para 
        percorrer cada linha

        '''
        return transposta
    
    except Exception as erro:
        print(f'erro encontrado: {erro}')

exemplo = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

for linha in transpor_matrix(exemplo):
    print(linha)
