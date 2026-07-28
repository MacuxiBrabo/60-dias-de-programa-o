# nesse arquivo vou criar um gerador de senhas particulas

import random # esse lib para pegar os elementos aleatoriamente
import string # esse para pegar todas as string

def gerador_senha(parametro):
    try:

        comprimento = parametro

        caracteris = string.ascii_letters + string.digits + string.punctuation
        senha = ''

        while len(senha) != comprimento:
            letra = random.choice(caracteris)

            senha = senha + letra

        print('essa é a sua senha -> ', senha)

    except Exception as erro:
        print('erro encontrado: ', erro)

    return None

gerador_senha(8)