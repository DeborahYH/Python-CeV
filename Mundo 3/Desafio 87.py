# Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado.
# O programa deve mostrar a matriz ncom a formatação correta.

# No final, mostre:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.

# [0,0,0]: uso de zeros dispensa o uso do append

matriz = [[0,0,0,],[0,0,0,],[0,0,0]]
soma_par = soma_col = maior = 0

# lê os elementos da matriz
for linha in range(0,3):
  for coluna in range(0,3):
    matriz[linha][coluna] = int(input(f"Digite um valor para a posição[{linha},{coluna}]: "))

# exibe a matriz na estrutura 3x3
# print() quebra a linha da matriz
# :^5: usa5 espaços + valor centralizado
for linha in range(0,3):
  for coluna in range(0,3):
    print(f"[{matriz[linha][coluna]:^5}]", end="")
    # avalia se o valor é par para somá-lo
    if matriz[linha][coluna] % 2 == 0:
      soma_par += matriz[linha][coluna]
    print()

# percorre a última coluna somando seus elementos
for linha in range(0,3):
  soma_col += matriz[linha][2]

# percorre a 2ª linha procurando o maior elemento
for coluna in range(0,3):
  if coluna == 0:
    maior = matriz[1][coluna]
  elif matriz[1][coluna] > maior:
    maior = matriz[1][coluna]

print("=" * 50)
print(f"A soma dos valores pares é igual a {soma_par}.")
print(f"A soma dos valores da 3ª coluna é igual a {soma_col}")
print(f"O maior valor da 2ª linha é igual a {maior}")
