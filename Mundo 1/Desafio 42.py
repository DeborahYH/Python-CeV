r1 = float(input("Comprimento da reta 1: "))
r2 = float(input("Comprimento da reta 2: "))
r3 = float(input("Comprimento da reta 3: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print("As retas formam um triângulo")
else:
  print("As retas não formam um triângulo")
if r1 == r2 and r2 == r3 and r1 == r3:
  print("O triângulo é equilátero")
elif r1 == r2 or r2 == r3 or r1 == r3:
  print("O triângulo é isósceles")
elif r1 != r2 and r2 != r3 and r1 != r3:
  print("O triângulo é escaleno")
