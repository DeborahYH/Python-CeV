# Desafio 93:
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.

time = list()
jogador = dict()
partidas = list()

while True:
  jogador.clear()
  jogador["nome"] = str(input("Nome do Jogador: "))
  total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
  partidas.clear()

  for cont in range(0, total):
    partidas.append(int(input(f"Quantos gols foram feitos na partida {cont+1}? ")))
  jogador["gols"] = partidas[:]
  jogador["total"] = sum(partidas)
  time.append(jogador.copy())

  while True:
      continua = str(input("Deseja continuar? [S/N]: ")).upper()[0]
      if continua in "SN":
        break
      else:
        print("Erro! Responda apenas S ou N")
  if continua == "N":
    break


print("="*40)
print("CÓDIGO ", end="")
for chave in jogador.keys():
  print(f"{chave:<15}", end="")
print()

print("="*40)
for chave, valor in enumerate(time):
  print(f"{chave:>4}: ", end="")
  for dado in valor.values():
    print(f"{str(dado):<15}", end="")
  print()
print("="*40)

while True:
  busca = int(input("Deseja exibir dados de qual jogador? (digite 999 para interromper): "))
  if busca == 999:
    break
  if busca >= len(time):
    print(f"ERRO - Não existe um jogador com código {busca}!")
  else:
    print(f"Levantamento do Jogador {time[busca]['nome']}:")
    for indice, n_gols in enumerate(time[busca]['gols']):
      print(f"Jogo {indice+1}: {n_gols}")
  print("=" * 40)

