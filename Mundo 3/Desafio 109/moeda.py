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


