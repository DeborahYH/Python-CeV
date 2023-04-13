# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
# o maior número no dado.

from random import randint
from operator import itemgetter

resultado = {"Jogador 1": randint(1,20),
             "Jogador 2": randint(1,20),
             "Jogador 3": randint(1,20),
             "Jogador 4": randint(1,20)}

print("VALORES SORTEADOS")
for k,v in resultado.items():
  print(f"O Jogador {k} sorteou o valor {v}.")

ranking = list()
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)
print()
print("========= RANKING =========")
for i,v in enumerate(ranking):
  print(f"{i+1}º Lugar: {v[0]} com {v[1]}")

  
