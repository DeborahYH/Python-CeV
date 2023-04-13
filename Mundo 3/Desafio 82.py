# Crie um programa que leia vários números e coloque-os em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
  n = int(input("Insira um valor: "))
  lista.append(n)
  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)
  continua = str(input("Deseja continuar? [S/N]: "))
  if continua in "Nn":
    break

print("="*30)
print(f"A lista completa é: {lista}")
print(f"A lista de números pares é: {pares}")
print(f"A lista de números ímpares é: {impares}")

# usar laços para percorrer a lista inicial
# usar append if para definir para qual lista os valores vão
