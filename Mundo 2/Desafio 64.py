n = 0
s = 0
c = 0
while n != 999:
  n = int(input("Digite um número [digite 999 para parar]: "))
  if n < 999:
    c += 1
    s += n
print("Você digitou {} números e a soma deles foi {}" .format(c,s))
  
