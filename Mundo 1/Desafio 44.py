preco = float(input("Insira o preço do produto: "))
print("Considere as opções abaixo:")
print("[1]: à vista em dinheiro/cheque")
print("[2]: à vista no cartão")
print("[3]: até 2x no cartão")
print("[4]: mais de 3x no cartão")
pgto = int(input("Insira a forma de pagamento: "))
if pgto == 1:
  print("Você deverá pagar R${:.2f}" .format(preco - preco*10/100))
elif pgto == 2:
  print("Você deverá pagar R${:.2f}" .format(preco - preco*5/100))
elif pgto == 3:
  print("Você deverá pagar 2 parcelas de R${:.2f}" .format(preco/2))
elif pgto == 4:
  precof = preco + (preco*20/100)
  parcelas = int(input("Em quantas parcelas a compra será paga?"))
  print("Você deverá pagar {} parcelas de R${:.2f}" .format(parcelas, precof))
else:
  print("Opção inválida. Tente novamente.")

