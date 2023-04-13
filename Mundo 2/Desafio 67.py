n = 0

while True:
  n = int(input("Deseja ver a tabuada de qual número? "))
  if n < 0:
    break
  for c in range(1,11):
    print(f"{c} X {n} = {c*n}")
print("PROGRAMA TABUADA ENCERRADO")
