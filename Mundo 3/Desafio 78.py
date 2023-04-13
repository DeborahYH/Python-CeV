# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

lista = []
maior = 0
menor = 0
pos_maior = 0
pos_menor = 0

for index in range(0,5):
  n = int(input("Digite um número: "))
  lista.append(n)
  if index == 0:
    maior = menor = lista[index]
  else:
    if n > maior:
      maior = n
      pos_maior = (index+1)
    if n < menor:
      menor = n
      pos_menor = (index+1) 
    
print(f"Os valores inseridos foram {lista}")
print(f"O maior valor inserido foi {maior}, na posição {pos_maior}")
print(f"O menor valor inserido foi {menor}, na posição {pos_menor}")
