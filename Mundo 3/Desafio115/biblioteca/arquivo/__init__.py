from Desafio115.biblioteca.interface import *

def arquivo_existe(nome):
    try:
        item = open(nome, 'rt')
        item.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        item = open(nome, 'wt+')
        item.close()
    except:
        print("Erro ao criar arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def ler_arquivo(nome):
    try:
        item = open(nome, 'rt')
    except:
        print("Erro ao abrir o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(item.read())
    finally:
        item.close()

def cadastrar(nome_arquivo, nome = 'Desconhecido', idade = 0):
    try:
        item = open(nome_arquivo, 'at')
    except:
        print("Erro ao abrir o arquivo")
    else:
        try:
            item.write(f'{nome}: {idade} \n')
        except:
            print("Erro ao cadastrar os dados")
        else:
            print(f"Cadastro de {nome} realizado com sucesso")
            item.close()

