# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):
    for valor in range(inicio, fim, passo):
        print(valor, " ", end="")

print("Contagem de 1 a 10. Intervalo = 1")
for valor in range(1,10,1):
    print(valor, " ", end="")
print()
print()

print("Contagem de 10 a 0. Intervalo = -2")
for valor in range(10,0,-2):
    print(valor, " ", end="")
print()
print()

print("Contagem Personalizada:")
primeiro = int(input("Insira o valor de início: "))
ultimo = int(input("Insira o valor final: "))
intervalo = int(input("Insira o valor do intervalo: "))
print("Os valores selecionados são:")
contador(primeiro, ultimo, intervalo)

