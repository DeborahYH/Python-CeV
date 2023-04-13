# Crie um programa contendo uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ("armario", "periquito", "lixeira", "refrigerante", "tapete")
vogais = 0
for palavra in tupla:
  print(f"\nNa palavra {palavra} temos ", end="")
  for letra in palavra:
    if letra.lower() in "aeiou":
      print(letra, end=" ")
