# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108

import moeda

preco = float(input("Digite o preço: "))
aumento = int(input("Deseja aumentar quantos %? "))
diminuicao = int(input("Deseja diminuir quantos %? "))

print(f"O dobro de {moeda.padrao(preco)} é {moeda.dobro(preco, True)}")
print(f"A metade de {moeda.padrao(preco)} é {moeda.metade(preco, True)}")
print(f"Aumentando {aumento}% teremos {moeda.aumentar(preco, aumento, True)}")
print(f"Diminuindo {diminuicao}% teremos {moeda.diminuir(preco, diminuicao, True)}")


