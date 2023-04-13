# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = dict()

boletim["Nome"] = str(input("Insira seu nome: "))
boletim["Média"] = float(input("Insira o valor da sua média: "))

if boletim["Média"] < 5:
  boletim["Situação"] = "Reprovado"
elif 5 <= boletim["Média"] <= 7:
  boletim["Situação"] = "Recuperação"
else:
  boletim["Situação"] = "Aprovado"

print()
print("===== SITUAÇÃO DO ALUNO ======")
for k,v in boletim.items():
  print(f"{k}: {v}")
