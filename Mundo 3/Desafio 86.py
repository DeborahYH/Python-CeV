# Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# [0,0,0]: uso de zeros dispensa o uso do append

matriz = [[0,0,0],[0,0,0],[0,0,0]]

# lê os elementos da matriz
for linha in range(0,3):
  for coluna in range(0,3):
    matriz[linha][coluna] = int(input(f"Digite um valor para a posição[{linha},{coluna}]: "))

# exibe a matriz na estrutura 3x3
for linha in range(0,3):
  for coluna in range(0,3):
    print(f"[{matriz[linha][coluna]:^5}]", end="")
  print()

# print() quebra a linha da matriz
# :^5: usa 5 espaços + valor centralizado
