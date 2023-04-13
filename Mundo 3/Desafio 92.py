# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com a idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário.
# Calcule e acrescente com quantos anos a pessoa vai se aposentar

from datetime import datetime

dados = dict()
dados["Nome"] = str(input("Nome: "))
nascimento = int(input("Ano de Nascimento: "))
dados["Idade"] = datetime.now().year - nascimento
dados["CTPS"] = int(input("Carteira de Trabalho (digite 0 se não tiver): "))

if dados["CTPS"] != 0:
  dados["Contratação"] = int(input("Ano de Contratação: "))
  dados["Salário"] = float(input("Salário: R$ "))
  dados["Aposentadoria"] = dados["Idade"]+((dados["Contratação"] + 35) - datetime.now().year)

print("="*30)
for k,v in dados.items():
  print(f"{k} : {v}")

