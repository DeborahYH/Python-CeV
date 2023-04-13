# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(mensagem):
    comprimento = len(mensagem)
    print("=" * comprimento)
    print(mensagem)
    print("=" * comprimento)

texto = str(input("Insira a mensagem a ser exibida: "))
escreva(texto)

