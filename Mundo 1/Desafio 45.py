import random
pedra = 1
papel = 2
tesoura = 3
l = [1,2,3]
pc = random.choice(l)
print("Escolha entre as opções abaixo:")
print("[1] = pedra")
print("[2] = papel")
print("[3] = tesoura")
escolha = int(input("Insira a opção escolhida: "))
if pc == escolha:
  print("Empate. Os dois escolheram {}." .format(pc))
elif pc == 1 and escolha == 3 or pc == 2 and escolha == 1 or pc == 3 and escolha == 2:
  print("O computador jogou {}.Você perdeu." .format(pc))
elif pc == 1 and escolha == 2 or pc == 2 and escolha == 3 or pc == 3 and escolha == 1:
  print("O computador jogou {}. Você venceu." .format(pc))

