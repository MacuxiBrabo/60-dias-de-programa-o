#nesse dia vou criar uma função que escreve e ler um arquivo de texto

def escrever_texto(nome_arquivo, texto):
    try:

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(texto)

        return print('Arquivo alterado!')

    except Exception as erro:
        print('Erro encontrado:', erro)

def ler_arquivo(nome_arquivo):
    try:

        with open(nome_arquivo, 'r') as arquivo:
            conteudo_arquivo = arquivo.read()
        return print(f'Conteúdo do texto:\n {conteudo_arquivo}')

    except FileNotFoundError as erro:
        print('O arquivo não foi encontrado')
    except Exception as erro:
        print('Erro encontrado:', erro)

def main(nome_arquivo, texto):
    try:

        print('Ola!, o que deseja?\n')

        while True:
            print('Digite 1 para gravar o texto no arquivo')
            print('Digite 2 para ler o arquivo')

            resposta = input('->')

            if resposta.strip().lower() == '1':
                print('Vamos gravar o texto no arquivo')
                escrever_texto(nome_arquivo, texto)
                break

            if resposta.strip().lower() == '2':
                print('Vamos ler o arquivo')
                ler_arquivo(nome_arquivo)
                break

            else:
                print('Opção incorreta, tente novamente\n')

    except Exception as erro:
        print('Erro encontrado:', erro)

if __name__ == '__main__':
    arquivo = 'arquivo.txt'
    texto = 'programação é bacana'
    main(arquivo, texto)