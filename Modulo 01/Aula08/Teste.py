try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")
except ValueError:
    print("Você precisa digitar um número válido!")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
