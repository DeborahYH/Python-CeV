# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando-os em uma lista composta.

# Laço for: considerar o numero inserido para gerar todos os jogos
# A cada laço fazer o append dos numeros em uma lista

from random import randint

print("="*30)
print("MEGA SENA")
print("="*30)
n_jogos = int(input("Quantos jogos deseja sortear? "))
print(f"Sorteando {n_jogos} jogos:")

tot_jogos = 1
lista_jogos = []
jogo_sort = []
cont = 0

# Sorteia os jogos até o limite definido pelo usuário
while tot_jogos <= n_jogos:
  cont = 0
  
  while True:
    num = randint(1,60)
    # Adiciona o número à lista jogo_sort apenas se ele já não estiver na lista
    # Justificativa: impede que os números se repitam
    if num not in jogo_sort:
      jogo_sort.append(num)
      cont += 1
    # Limita o número de elementos da lista em 6
    if cont >= 6:
      break
    
  # Coloca os números sorteados em ordem crescente
  jogo_sort.sort()
  # Cria uma cópia da lista jogo_sort antes de apagá-la
  # Resultado: cria uma lista contendo todos os sorteios separados
  lista_jogos.append(jogo_sort[:])
  jogo_sort.clear()
  tot_jogos += 1

for indice, lista in enumerate(lista_jogos):
  print (f"Jogo {indice + 1} : {lista}")




  
