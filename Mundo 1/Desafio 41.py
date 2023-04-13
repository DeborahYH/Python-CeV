from datetime import date
nasc = int(input("Insira o ano de nascimento: "))
idade = (date.today().year) - nasc
print("Você tem", idade, "anos")
if idade <= 9:
  print("Você pertence à categoria Mirim")
elif idade > 9 and idade <= 14:
  print("Você pertence à categoria Infantil")
elif idade > 14 and idade <= 19:
  print("Você pertence à categoria Junior")
elif idade > 19 and idade <= 20:
  print("Você pertence à categoria Sênior")
else:
  print("Você pertence à categoria Master")
