# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário deseja continuar.
# No final, mostre:
# - qual é o total gasto na compra.
# - quantos produtos custam mais de R$1000.
# - qual é o nome do produto mais barato.

total = 0
mais1000 = 0
barato = ""
menorpreco = 0
contador = 0
continua = ""
while True:
  nome = str(input("Insira o nome do produto: "))
  preco = float(input("Insira o preço do produto: "))
  contador += 1
  total += preco
  if preco > 1000:
      mais1000 += 1
  if contador == 1:
    menorpreco = preco
    barato = nome
  else:
    if preco < menorpreco:
      menorpreco = preco
      barato = nome
  continua = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
  if continua == "N":
    break
print(f"O total da compra foi R${total:.2f}")
print(f"Foram contabilizados {mais1000} produtos que custam mais de R$1000,00")
print(f"O produto mais barato é o/a {barato},que custa R${menorpreco:.2f}")
  

