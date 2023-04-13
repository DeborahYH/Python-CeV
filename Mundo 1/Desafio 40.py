n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media = (n1 + n2) / 2
print("Sua média é {:.1f}." .format(media))
if media < 5:
  print("Você foi reprovado")
elif media >= 5 and media < 7:
  print("Você está de recuperação")
else:
  print("Você foi aprovado")
