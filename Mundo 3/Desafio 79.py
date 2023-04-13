# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
  n = int(input("Digite um valor: "))
  if n not in numeros:
    numeros.append(n)
  else:
    print("Este número já foi inserido")
  continua = str(input("Deseja Continuar? [S/N]: "))
  if continua in "Nn":
    break

numeros.sort()
print(f"A lista criada é: {numeros}")
  
