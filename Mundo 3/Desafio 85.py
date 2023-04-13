# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

todos = list()
pares = list()
impares = list()

for valor in range(1,7):
  v = int(input("Insira um valor: "))
  todos.append(v)
  if v % 2 == 0:
    pares.append(v)
  else:
    impares.append(v)

pares.sort()
impares.sort()
print(f"Os valores digitados foram {todos}")
print(f"Os valores pares, em ordem crescente, são: {pares}")
print(f"Os valores impares, em ordem crescente, são: {impares}")
