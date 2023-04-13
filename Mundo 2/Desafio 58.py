import random
lista = [0,1,2,3,4,5,6,7,8,9,10]
comp_num = random.choice(lista)
tent = 1

print("Olá! Eu sou seu computador!")
print("Acabei de pensar em um número entre 0 e 10.")
print("Você consegue adivinhar qual foi?")
num = int(input("Qual é o seu palpite? "))
  
while comp_num != num:
  if num < comp_num:
    print("Mais...Tente mais uma vez.")
    num = int(input("Qual é o seu palpite? "))
    tent += 1
  else:
    print("Menos...Tente mais uma vez.")
    num = int(input("Qual é o seu palpite? "))
    tent += 1
    
print("Você acertou com {} tentativas" .format(tent))
