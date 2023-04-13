def dobro(valor = 0, formatar = False):
    resultado = valor * 2
    if formatar == False:
        return resultado
    else:
        return padrao(resultado)

def metade(valor = 0, formatar = False):
    resultado = valor / 2
    if formatar == False:
        return resultado
    else:
        return padrao(resultado)

def aumentar(valor = 0, taxa = 0, formatar = False):
    resultado = valor + (valor * taxa/100)
    if formatar == False:
        return resultado
    else:
        return padrao(resultado)

def diminuir(valor = 0, taxa = 0, formatar = False):
    resultado = valor - (valor * taxa/100)
    if formatar == False:
        return resultado
    else:
        return padrao(resultado)

def padrao(valor = 0, moeda = 'R$', formatar = False):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(valor = 0, taxa_aumento = 10, taxa_diminuicao = 5):
    print('='*35)
    print('VALOR - RESUMO'.center(35))
    print('='*35)
    print(f'Preço Analisado: \t\t{padrao(valor)}')
    print(f'Dobro do Preço: \t\t{dobro(valor,True)}')
    print(f'Metade do Preço: \t\t{metade(valor,True)}')
    print(f"Aumentando {taxa_aumento}% teremos \t{aumentar(valor, taxa_aumento, True)}")
    print(f"Diminuindo {taxa_diminuicao}% teremos \t{diminuir(valor, taxa_diminuicao, True)}")
    print('='*35)

