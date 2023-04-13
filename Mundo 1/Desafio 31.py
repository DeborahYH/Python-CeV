distancia = float(input("Insira a distância da viagem: "))
if distancia <=200:
  preco = distancia * 0.50
else:
  preco = distancia * 0.45
print("O preço da sua passagem será de R${:.2f}" .format(preco))
