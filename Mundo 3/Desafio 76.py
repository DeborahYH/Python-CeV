# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

objetos = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.70, "Estojo", 25,
           "Transferidor", 4.20, "Compasso", 9, "Mochila", 120.30,
           "Caneta", 2.50, "Livro", 40)

for item in range(0,(len(objetos))):
  if item % 2 == 0:
    print(f"{objetos[item]:.<30}", end="")
  else:
    print(f"R${objetos[item]:>5.2f}")

