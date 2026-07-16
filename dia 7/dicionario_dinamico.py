# nesse arquivo vou criar um ducionário dinâmico

aluno = {}

aluno['ID da matrícula'] =  input('digite o ID do aluno: ')
aluno['nome'] = input('digite o nome do aluno: ')
aluno['idade'] = int(input('digite a idade do aluno: ')) 
aluno['curso'] = input('digite o curso do aluno: ')

for chave, item in aluno.items():
    print(f'{chave} -> {item}')