n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
opcao = 0

while opcao != 5:
  print("[1] somar")
  print("[2] multiplicar")
  print("[3] maior")
  print("[4] novos números")
  print("[5] sair do programa")
  opcao = int(input("Qual é a sua opção? "))
  if opcao == 1:
    soma = n1 + n2
    print("A soma dos dois valores resulta em", soma)
    print("=-"*10, "=")
  elif opcao == 2:
    mult = n1 * n2
    print("O produto dos dois valores é", mult)
    print("=-"*10, "=")
  elif opcao == 3:
    if n1 > n2:
      maior = n1
      print("Entre {} e {} o maior valor é {}" .format(n1, n2, maior))
      print("=-"*10, "=")
    else:
      maior = n2
      print("Entre {} e {} o maior valor é {}" .format(n1, n2, maior))
      print("=-"*10, "=")
  elif opcao == 4:
    print("Informe os números novamente")
    n1 = str(input("Insira o primeiro valor: "))
    n2 = str(input("Insira o segundo valor: "))
  elif opcao == 5:
    print("Fim do programa. Volte sempre!")
  else:
    print("Opção inválida. Tente novamente.")
  
