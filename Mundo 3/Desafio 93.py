# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()

jogador["nome"] = str(input("Nome do Jogador: "))
total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for cont in range(0,total):
  partidas.append(int(input(f"Quantos gols foram feitos na partida {cont}? ")))
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)

print("="*20)

for key,value in jogador.items():
  print(f"O campo {key} tem o valor {value}.")

print("="*20)

print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for index,value in enumerate(jogador["gols"]):
  print(f"Na partida {index} fez {value} gols.")
print(f"Total de gols: {jogador['total']}")
  
