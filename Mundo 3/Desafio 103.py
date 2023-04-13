# Crie uma função chamada ficha(), que recebe dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome="<desconhecido>", gols = 0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

nome_jogador = str(input("Nome do Jogador: "))
numero_gols = str(input("Número de Gols: "))
if numero_gols.isnumeric():
    numero_gols = int(numero_gols)
else:
    numero_gols = 0

if nome_jogador.strip() == '':
    ficha(gols = numero_gols)
else:
    ficha(nome_jogador, numero_gols)



