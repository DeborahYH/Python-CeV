# Crie um programa contendo uma tupla totalmente preenchida
# por uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número entre 0-20 pelo teclado
# e mostrá-lo por extenso.

t = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
     "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
     "dezoito", "dezenove", "vinte")

while True:
  n = int(input("Insira um número entre 0 e 20: "))
  if 0< n < 20:
    break
  print("Tente novamente.", end="")

print(f"Você inseriu o número {t[n]}")
