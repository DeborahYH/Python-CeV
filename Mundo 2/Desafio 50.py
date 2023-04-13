s = 0
p = 0
for c in range(1, 7):
  n = int(input("Insira um número: "))
  if n%2 == 0:
    s += n
    p += 1
print("Você inseriu {} números pares cuja soma é igual a {}" .format(p,s))
