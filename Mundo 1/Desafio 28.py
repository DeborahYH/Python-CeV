from random import randint
computador = randint(0,5)
print("-=-" * 20)
print("Vou pensar em um número entre 0-5. Tente advinhar")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))
if jogador == computador:
  print("Parabéns! Você advinhou!")
else:
  print("Errado! Eu pensei no número {} e não no número {}" .format(computador, jogador))
