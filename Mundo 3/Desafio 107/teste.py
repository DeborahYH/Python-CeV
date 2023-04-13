# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

preco = float(input("Digite o preço: "))
aumento = int(input("Deseja aumentar quantos %? "))
diminuicao = int(input("Deseja diminuir quantos %? "))

print(f"O dobro de R${preco} é R${moeda.dobro(preco)}")
print(f"A metade de R${preco} é R${moeda.metade(preco)}")
print(f"Aumentando {aumento}% teremos R${moeda.aumentar(preco, aumento)}")
print(f"Diminuindo {diminuicao}% teremos R${moeda.diminuir(preco, diminuicao)}")


