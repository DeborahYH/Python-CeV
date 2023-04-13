i = 0
s = 0
for c in range (1, 501):
  if c%2 != 0:
    if c%3 == 0:
      i = i + 1
      s = s + c
print("A soma dos {} valores é igual a {}" .format(i, s))
