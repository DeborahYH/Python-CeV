print("-"*20)
print("SEQUÊNCIA DE FIBONACCI")
print("-"*20)
n = int(input("Quantos valores da sequência você deseja mostrar? "))
t1 = 0
t2 = 1
print("{} --> {}" .format(t1, t2), end="")
cont = 3
while cont <= n:
  t3 = t1 + t2
  print(" --> {}" .format(t3), end="")
  t1 = t2
  t2 = t3
  cont += 1
print(" --> FIM")
