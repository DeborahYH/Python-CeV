n = 0
c = 0
soma = 0
maior = 0
menor = 0
conti = "s"
while conti != "n":
  n = int(input("Digite um número: "))
  conti = str(input("Quer continuar? [s/n]: "))
  c += 1
  soma += n
  media = soma/c
  if c == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
print("Você digitou {} números e a média foi {}" .format(c,media))
print("O maior valor foi {} e o menor valor foi {}" .format(maior,menor))
