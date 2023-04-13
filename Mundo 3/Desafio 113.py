# Reescreva a função leiaInt() do desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido.
# Crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(valor):
    while True:
        try:
            n = int(input(valor))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido. \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interrompida pelo usuário. \033[m")
            return 0
        else:
            return n


def leiaReal(valor):
    while True:
        try:
            n = float(input(valor))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número real válido. \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interrompida pelo usuário. \033[m")
            return 0
        else:
            return n

numero1 = leiaInt("Digite um número inteiro: ")
numero2 = leiaReal("Digite um número real: ")
print(f"Você digitou os valores {numero1} e {numero2}")



