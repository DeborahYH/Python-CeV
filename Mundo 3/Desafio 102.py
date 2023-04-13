# Crie uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
# e outro chamado show (opcional), que será um valor lógico indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: número a ser calculado
    :param show: define se o cálculo do fatorial é exibido (opcionial)
    :return: valor do fatorial de numero
    """
    resultado = 1
    for c in range(numero, 0, -1):
        resultado *= c
    if show == True:
        for c in range(numero, 0, -1):
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
                print(resultado)
    return resultado

help(fatorial)
n = int(input("Insira um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n, show=True)}")


