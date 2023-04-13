from datetime import date
maior = 0
menor = 0
for c in range(1,8):
  ano = int(input("Insira o ano em que a 1a pessoa nasceu: "))
  if date.today().year - ano < 18:
    menor += 1
  else:
    maior += 1
print("Ao todo tivemos {} pessoas maiores de idade" .format(maior))
print("E também tivemos {} pessoas menores de idade" .format(menor))
