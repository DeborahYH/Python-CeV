# Crie uma função chamada voto() que recebe como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
import datetime

ano_atual = datetime.date.today().year

def voto(ano_nasc, idade):
    categoria = ""
    if idade < 16:
        categoria = "VOTO NEGADO"
    elif idade >= 16 and idade < 18 or idade > 70:
        categoria = "VOTO OPCIONAL"
    elif idade >= 18 and idade <= 70:
        categoria = "VOTO OBRIGATÓRIO"
    return categoria

ano_nascimento = int(input("Insira o ano do seu nascimento: "))
idade = ano_atual - ano_nascimento
print(f"Idade: {idade} anos")
print(voto(ano_nascimento, idade))

