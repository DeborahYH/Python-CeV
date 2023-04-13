# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou.

import random
computador = ""
vitoria = 0
lista = [1,2,3,4,5,6,7,8,9,10]

while True:
  usuario = str(input("Escolha par/impar: "))
  if usuario == "par":
    computador = "impar"
  elif usuario == "impar":
    computador = "par"
  print(f"Você escolheu {usuario}")
  print(f"O computador escolheu {computador}")
  n_usuario = int(input("Escolha um número: "))
  n_computador = random.choice(lista)
  print(f"Você jogou o número {n_usuario}")
  print(f"O computador jogou o número {n_computador}")
  soma = n_usuario + n_computador
  if usuario == "par" and soma % 2 == 0 or usuario == "impar" and soma % 2 != 0:
    print(f"A soma dos dois números é {soma}. Você venceu!")
    vitoria += 1
  else:
    print(f"A soma dos dois números é {soma}. Você perdeu...")
    break
print(f"Você obteve {vitoria} consecutivas.")
 

