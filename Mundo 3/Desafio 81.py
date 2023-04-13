# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
  n = int(input("Insira um número: "))
  lista.append(n)
  continua = str(input("Deseja continuar? [S/N]: "))
  if continua in "Nn":
    break

print(f"A lista criada foi: {lista}")
print(f"Foram digitados {len(lista)} números")
lista.sort(reverse = True)
print(f"Esta é a lista em ordem crescente: {lista}")
if 5 in lista:
  print("O valor 5 está na lista")
else:
  print("O valor 5 não está na lista")
