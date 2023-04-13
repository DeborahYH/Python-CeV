# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

import random

def comparador(*valores):
    maior_numero = 0
    tamanho = 0
    for numero in valores:
        tamanho += 1
        if numero > maior_numero:
            maior_numero = numero
    print(f"Os valores fornecidos foram {valores}")
    print(f"Foram informados {tamanho} valores ao todo.")
    print(f"O maior valor informado foi {maior_numero}")

tamanho = random.randrange(3, 10)
numeros = []

for indice in range(0, tamanho):
    indice = random.randint(1, 100)
    numeros.append(indice)
print(numeros)

comparador(*numeros)

