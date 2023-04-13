# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno


def area(larg,comp):
    area = larg * comp
    print(f"Este terreno tem {area} m2")

print("CÁLCULO DA ÁREA DO TERRENO")
largura = (float(input("Largura (m): ")))
comprimento = (float(input("Comprimento (m): ")))
area(largura, comprimento)

