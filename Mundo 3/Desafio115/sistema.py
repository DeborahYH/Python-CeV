from Desafio115.biblioteca.interface import *
from Desafio115.biblioteca.arquivo import *

arquivo = 'curso.txt'
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        ler_arquivo(arquivo)
    elif resposta == 2:
        cabecalho("Novo Cadastro")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        print('Saindo do Sistema')
        break
    else:
        print("Erro! Digite uma opção válida")


