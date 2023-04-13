c = 0
s = 0

while True:
  n = int(input("Insira um número inteiro: "))
  if n == 999:
    break
  c += 1
  s += n
print(f"Foram digitados {c} números cuja soma é igual a {s}")
