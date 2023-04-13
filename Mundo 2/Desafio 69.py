# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada cadastro, o programa deverá perguntar se o usuário deseja continuar.
# No final, mostre:
# - quantas pessoas tem mais de 18 anos.
# - quantos homens foram cadastrados.
# - quantas mulheres tem menos de 20 anos.

maior18 = 0
sexo = ""
homens = 0
f_menor20 = 0
continua = ""

while True:
  idade = int(input("Insira a sua idade: "))
  if idade > 18:
    maior18 += 1
  sexo = str(input("Insira o seu sexo [F/M]: ")).strip().upper()[0]
  if sexo == "M":
    homens += 1
  if sexo == "F" and idade < 20:
    f_menor20 += 1
  continua = str(input("Deseja continuar [S/N]?: ")).strip().upper()[0]
  if continua == "N":
    break

print(f"{maior18} pessoas tem mais de 18 anos.")
print(f"Foram cadastrados {homens} homens.")
print(f"Foram cadastradas {f_menor20} mulheres com menos de 20 anos.")



