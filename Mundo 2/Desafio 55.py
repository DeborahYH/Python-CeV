mai_peso = 0
men_peso = 0

for c in range (1,6):
  peso = float(input("Insira o seu peso: "))
  if c == 1:
    mai_peso = peso
    men_peso = peso
  else:
    if peso > mai_peso:
      mai_peso = peso
    if peso < men_peso:
      men_peso = peso
  
print(mai_peso)
print(men_peso)
