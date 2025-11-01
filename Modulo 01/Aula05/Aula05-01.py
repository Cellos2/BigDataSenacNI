print("--- Usando FOR (Repetição Contada) ---")

# O range(5) gera os números 0, 1, 2, 3, 4 (5 repetições)
for i in range(5):
    try:
        # i representa o número atual da repetição (0, 1, 2...)
        print(f"Número {i + 1} de 5:")
        num = float(input("Digite um número: "))

        dobro = num * 2
        triplo = num * 3
        quadruplo = num * 4

        print(f"Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quadruplo}\n")

    except ValueError:
        print("Entrada inválida. Tente novamente.\n")