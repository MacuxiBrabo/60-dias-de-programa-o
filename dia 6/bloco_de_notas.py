# Hoje vou criar um bloco de notas com tudo que já aprendi

print('=' * 40, '\n')
print('Olá, esse é o seu bloco de notas \nanote o que precisar e o que quiser. \nQuando quiser sair, Digite "sair" para fechar o bloco de notas.\n')
print('=' * 40, '\n')

bloco_de_notas = []

while True: 
    entrada = input('Digite aqui -> ')
    if entrada == 'sair':
        break
    else:
        bloco_de_notas.append(entrada)
    
    print('=' * 40, '\n')

    for item in bloco_de_notas:
        print('-', item)

    print('=' * 40, '\n')

print('=' * 40, '\n')

for item in bloco_de_notas:
    print('-', item)

print('=' * 40, '\n')
    