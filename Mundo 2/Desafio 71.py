# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# O programa irá então informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

saque = int(input("Que valor deseja sacar? "))
total = saque
cedula = 50
tot_cedula = 0
while True:
  if total >= cedula:
    total -= cedula
    tot_cedula += 1
  else:
    print(f"Total de {tot_cedula} cédulas de R${cedula}")
    if cedula == 50:
      cedula = 20
    elif cedula == 20:
      cedula = 10
    elif cedula == 10:
      cedula = 1
    tot_cedula = 0
    if total == 0:
      break
