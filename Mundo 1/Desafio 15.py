dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantidade de km rodados: "))
pago = (dias * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}" .format(pago))
