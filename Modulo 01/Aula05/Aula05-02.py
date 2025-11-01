print("--- Usando WHILE (Repetição Condicional) ---")

contador = 0  # Inicializamos o contador
limite = 5    # Definimos o limite

while contador < limite:  # Condição de parada
    try:
        print(f"Número {contador + 1} de {limite}:")
        num = float(input("Digite um número: "))

        dobro = num * 2
        triplo = num * 3
        quadruplo = num * 4

        print(f"Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quadruplo}\n")

        contador = contador + 1  # Incrementa o contador para evitar loop

    except ValueError:
        print("Entrada inválida. Tente novamente.")
        # Não incrementa o contador aqui, pois o usuário deve tentar novamente