tot = 0
n = int(input("Insira um número inteiro: "))
for c in range(1, n+1):
  if n%c == 0:
    tot += 1
print("O número {} foi divisível {} vezes" .format(n, tot))
if tot == 2:
  print("Este é um número primo")
else:
  print("Este não é um número primo")
