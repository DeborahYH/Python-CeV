soma = 0
menor20 = 0
nome_velho = ""
idade_h = 0
for c in range (1,5):
  print("----- {}a PESSOA -----" .format(c))
  nome = str(input("Insira o seu nome: "))
  idade = int(input("Insira a sua idade: "))
  sexo = str(input("Insira o seu sexo (M/F): ")).strip()
  soma += idade
  media = soma/4
  if sexo == "F" and idade < 20:
    menor20 += 1
  if sexo == "M":
    idade_h = idade
    if idade > idade_h:
      idade_h = idade
      nome_velho = nome
print("A média de idade é", media)
print("Existem {} mulheres com menos de 20 anos no grupo" .format(menor20))
print("O homem mais velho se chama {} e tem {} anos" .format(nome_velho, idade_h))

