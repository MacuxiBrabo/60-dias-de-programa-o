# nesse programa, vou criar um verificador que análisa se um número é primo ou não(ou seja, composto)
try:

    numero = int(input('verifique se esse número é primo ou não(composto) -> '))

    e_primo = True

    if numero <= 1:
        e_primo = False
    else:
        for indice in range(2, int(numero ** 0.5) + 1):
            if numero % indice == 0:
                e_primo = False
                break

    if e_primo:
        print(f'o número {numero} é primo')
    else:
        print(f'o número {numero} é composto')

except Exception as erro:
    print('erro encontrado: ', erro)
