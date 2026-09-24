# nesse dia vou criar um conversor de moedas (de real para dolár e vice-versa)

def conversor_moeda(valor, taxa_cambio, taxa_conversao):

    try:

        if taxa_conversao == 'dolar_real':
            return round(valor * taxa_cambio, 2)
        
        elif taxa_conversao == 'real_dolar':
            return round(valor / taxa_cambio, 2)
        
        else:
            return ValueError('taxa de conversao inválida')
        
    except Exception as erro:
        print('erro encontrado: ', erro)

print(conversor_moeda(1, 0.19, 'real_dolar'))