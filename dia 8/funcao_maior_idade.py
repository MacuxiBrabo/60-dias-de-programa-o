# nesse arquivo, a condicional vai ser uma função

def maior_idade(idade):
    idade = int(idade)

    if idade >= 18:
        return 'maior de idade'
    
    else:
        return 'menor de idade'
    
try:
    pergunta = int(input('digite sua idade: '))

    print(maior_idade(pergunta))

except ValueError :
    print('insira a idade em números')