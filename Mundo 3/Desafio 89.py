# Crie um programa que leia o nome e duas notas de vários alunos e guarde
# tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que
# o usuário possa mostrar as notas de cada aluno individualmente.

# Cria 1 ficha para cada aluno
ficha = []
while True:
  nome = str(input("Nome: "))
  nota1 = float(input("Nota 1: "))
  nota2 = float(input("Nota 2: "))
  media = (nota1 + nota2) / 2
  ficha.append([nome, [nota1, nota2], media])
  resposta = str(input("Deseja continuar? [S/N]: "))
  if resposta in "nN":
    break

print("-=-"*20)

# Boletim
# No. com 4 caracteres alinhado à esquerda
# Nome com 10 caracteres alinhado à esquerda
# Média. com 8 caracteres alinhado à direita
# Ficha:[nota1, nota2] correspondem ao aluno[1]
for indice, aluno in enumerate(ficha):
  print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

while True:
  print("-=-"*20)
  opcao = int(input("Mostrar notas de qual aluno? (Digite 999 para interromper)"))
  if opcao == 999:
    print("Finalizando...")
    break
  if opcao <= len(ficha) - 1:
    print(f"As notas de {ficha[opcao][0]} são {ficha[opcao][1]}")
