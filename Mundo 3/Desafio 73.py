# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

rank = ("Atlético-MG", "Flamengo", "Palmeiras", "Corinthians", "Bragantino",
        "Fortaleza", "Fluminense", "América-MG", "Ceará-SC", "Internacional",
        "Santos", "São Paulo", "Atlético-GO", "Juventude", "Cuiabá",
        "Atlético-PR", "Bahia", "Grêmio", "Sport Recife", "Chapecoense")

print(f"Os 5 primeiros times são: {rank[0:5]}.")
print("=" *20)
print(f"Os últimos 4 colocados são: {rank[-4:]}")
print("=" *20)
print(f"Os 20 primeiros colocados, em ordem alfabética, são: {sorted(rank)}")
print("=" *20)
print(f"O Chapecoense está na {rank.index('Chapecoense')+1}a. posição.")
