try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    resultado = a / b
except (ValueError, TypeError):
    print("Houve um problema com os valores digitados")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados")
else:
    print(f"O resultado é igual a {resultado:.2f}")
finally:
    print("Finalizando...")


