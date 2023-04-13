def linha(tamanho = 40):
    return ('=' * tamanho)

def cabecalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())

def menu(lista):
    cabecalho('Menu Principal')
    contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1
    print(linha())
    opcao = int(input('Insira sua opção: '))
    return opcao

