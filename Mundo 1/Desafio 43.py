peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
imc = peso/altura**2
print("Seu IMC é {:.1f}" .format(imc))
if imc < 18.5:
  print("Você está abaixo do peso")
elif 18.5 <= imc < 25:
  print("Você está dentro da faixa de peso ideal")
elif 25 <= imc < 30:
  print("Você está com sobrepeso")
elif 30<= imc < 40:
  print("Você está obeso")
else:
  print("Você está com obesidade mórbida")
