# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

temporario = list()
dados = list()
cadastro = 0
pesado = leve = 0
p_pesado = ""
p_leve = ""

while True:
  nome = str(input("Nome: "))
  temporario.append(nome)
  peso = float(input("Peso: "))
  temporario.append(peso)
  dados.append(temporario[:])
  temporario.clear()
  
  if cadastro == 0:
    leve = peso
  else:
    if peso < leve:
      leve = peso
  if peso > pesado:
    pesado = peso
  cadastro += 1
  continua = str(input("Deseja continuar? [S/N]: "))
  if continua == "n" or continua == "N":
    break

for pessoa in dados:
  if dados[1] == leve:
    p_leve = dados[0][0]

for pessoa in dados:
  if dados[1] == pesado:
    p_pesado = dados[0][0]

print(dados)
print(f"Foram cadastradas {cadastro} pessoas.")
print(f"O maior peso registrado foi o de {p_pesado}, com {pesado}kg.")
print(f"O menor peso registrado foi o de {p_leve}, com {leve}kg.")

#não está mostrando o nome das pessoas. Verificar no python tutor
