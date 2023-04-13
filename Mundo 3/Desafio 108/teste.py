# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

import moeda

preco = float(input("Digite o preço: "))
aumento = int(input("Deseja aumentar quantos %? "))
diminuicao = int(input("Deseja diminuir quantos %? "))

print(f"O dobro de {moeda.padrao(preco)} é {moeda.padrao(moeda.dobro(preco))}")
print(f"A metade de {moeda.padrao(preco)} é {moeda.padrao(moeda.metade(preco))}")
print(f"Aumentando {aumento}% teremos {moeda.padrao(moeda.aumentar(preco, aumento))}")
print(f"Diminuindo {diminuicao}% teremos {moeda.padrao(moeda.diminuir(preco, diminuicao))}")


