# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.

import random

def sorteia(minimo,maximo):
    numeros = []
    for index in range(0, 5):
        valor = random.randint(minimo,maximo)
        numeros.append(valor)
    print(f"Os valores sorteados são:")
    print(numeros)
    return numeros

def somaPar(funcao):
    pares = []
    soma = 0
    for valor in funcao:
        if valor % 2 == 0:
            pares.append(valor)
            soma += valor
    if len(pares) > 0:
        print(f"Os valores pares sorteados são: {pares}")
    else:
        print(f"Não foram sorteados valores pares")
    print(f"A soma dos valores pares é {soma}")

somaPar(sorteia(1,100))


