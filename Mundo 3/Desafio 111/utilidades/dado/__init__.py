def leia_dinheiro(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',' , '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERRO: Preço Inválido!\033[m')
        else:
            valido = True
            return float(entrada)

