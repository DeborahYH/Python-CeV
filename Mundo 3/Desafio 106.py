# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores

cores = ('\033[m',              # 0 = sem cores
         '\033[0;30;41m',       # 1 = vermelho
         '\033[0;30;42m',       # 2 = verde
         '\033[0;30;43m',       # 3 = amarelo
         '\033[0;30;44m',       # 4 = azul
         '\033[0;30;45m',       # 5 = roxo
         '\033[0;37m')          # 6 = branco

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(cores[6], end='')
    help(comando)
    print(cores[0], end='')

def titulo(mensagem, cor = 0):
    tamanho = len(mensagem)
    print(cores[cor], end='')
    print('=' * tamanho)
    print(mensagem)
    print('=' * tamanho)
    print(cores[0], end='')

comando_a_pesquisar = ''
while True:
    titulo('SISTEMA DE AJUDA PY_HELP', 2)
    comando_a_pesquisar = str(input("Função ou Biblioteca: "))
    if comando_a_pesquisar.upper() == 'FIM':
        break
    else:
        ajuda(comando_a_pesquisar)
titulo('FINALIZANDO O SISTEMA', 1)



