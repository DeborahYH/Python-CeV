print("=" *30)
print((" "*5), "10 TERMOS DE UMA PA",(" "*5))
print("=" *30)

t1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Qual a razão da PA? "))
pt = (t1 + r)

print(t1, "--> ", end="")
print(pt, "--> ", end="")

for c in range (0,8):
  pt = pt + r
  print(pt, "--> ", end="")
print("Fim")
  
  

