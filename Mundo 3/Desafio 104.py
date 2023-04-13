# Crie a função leiaInt(), que deve funcionar de forma semelhante 'a função input() do Python,
# mas fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(valor):
    if valor.isnumeric() == False:
        print("\033[0;31mERRO! Digite um número inteiro válido. \033[m")
    else:
        print("Você acaba de digitar o número ", valor)


numero = leiaInt(input("Digite um número: "))


