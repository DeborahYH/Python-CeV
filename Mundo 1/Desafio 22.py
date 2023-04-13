nome = str(input("Insira seu nome completo: ")).strip()
print("Nome em maiúsculas: {} " .format(nome.upper()))
print("Nome em minúsculas: {} " .format(nome.lower()))
print("Seu nome tem {} letras" .format(len(nome)- nome.count(" ")))
print("Seu primeiro nome tem {} letras" .format(nome.find(" ")))

