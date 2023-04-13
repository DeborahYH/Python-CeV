print("=" *30)
print((" "*5),"10 TERMOS DE UMA PA",(" "*5))
print("=" *30)

t1 = int(input("Insira o primeiro termo da PA: "))
r = int(input("Qual a razão desta PA? "))
dec_prim = t1 + (11-1) * r

for c in range(t1, dec_prim, r):
  print("{} --> " .format(c), end="")
print("Fim")
  
