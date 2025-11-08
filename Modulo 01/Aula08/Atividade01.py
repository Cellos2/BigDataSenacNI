def calcular_multa(peso_total):
    """Calcula a multa com base no peso total pescado."""
    limite = 100
    valor_multa_por_kg = 4.0

    if peso_total > limite:
        excesso = peso_total - limite
        multa = excesso * valor_multa_por_kg
        return multa
    else:
        return 0.0


def registrar_pescarias():
    """Lê os pesos das pescarias e acumula o total de multas."""
    total_multa = 0.0

    while True:
        peso = float(input("Digite o peso pescado (ou 0 para encerrar): "))
        if peso == 0:
            break

        multa = calcular_multa(peso)

        if multa > 0:
            print(f"Você excedeu o limite! Multa a pagar: R$ {multa:.2f}")
        else:
            print("Peso dentro do limite. Nenhuma multa a pagar.")

        total_multa += multa

    return total_multa


def main():
    """Função principal do programa."""
    print("=== Controle de Pesca ===")
    total = registrar_pescarias()
    print(f"\nTotal de multa acumulado no dia: R$ {total:.2f}")


# Executa o programa
main()
