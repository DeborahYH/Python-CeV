# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os numa tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input("Insira um número: ")), int(input("Insira um número: ")),
         int(input("Insira um número: ")), int(input("Insira um número: ")))

print(f"Você inseriu os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
  print(f"O valor 3 apareceu pela primeira vez na posição {tupla.index(3)+1}")
else:
  print(f"O valor 3 não foi digitado")
print(f"Os números pares digitados são: ", end="")
for n in tupla:
  if n % 2 == 0:
    print(n, end="")
