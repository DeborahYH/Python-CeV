print("Gerador de PA")
print("="*20)
t1 = int(input("Primeiro Termo: "))
r = int(input("Razão da PA: "))
termo = t1
c = 1
print("PA: ", end="")

while c <= 10:
  print("{} --> " .format(termo), end="")
  termo += r
  c += 1
print("FIM")
