# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

grupo = list()
pessoa = dict()
soma = media = 0

while True:
  pessoa.clear
  pessoa["nome"] = str(input("Nome: "))

  while True:
    pessoa["sexo"] = str(input("Sexo (F/M): ")).upper()[0]
    if pessoa["sexo"] in "MF":
      break
    else:
      print("Erro! Por favor digite apenas 'F' ou 'M'")
    
  pessoa["idade"] = int(input("Idade: "))
  soma += pessoa["idade"]
  grupo.append(pessoa.copy())

  while True:
    resposta = str(input("Deseja continuar (S/N)? ")).upper()[0]
    if resposta in "SN":
      break
    else:
      print("Erro! Responda apenas 'S' ou 'N'")

  if resposta == "N":
    break

print("="*30)
print(f"Ao todo temos {len(grupo)} pessoas cadastradas")

media = soma/len(grupo)
print(f"A média de idade é {media:5.2f} anos.")

print(f"As mulheres cadastradas são: ", end="")
for p in grupo:
  if p["sexo"] in "Ff":
    print(f"{p['nome']}", end="")
print()

print(f"As pessoas cuja idade está acima da média são: ", end="")
for p in grupo:
  if p["idade"] >= media:
    for key,value in p.items():
      print(f"{key} = {value} ", end="")
    print()
print("<< ENCERRADO >>")
