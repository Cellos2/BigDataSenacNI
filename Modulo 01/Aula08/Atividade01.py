#1. Controle de Pesca
#Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
#traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
#pagar uma multa de R$ 4,00 por quilo excedente.
#● O programa deve ler o peso de peixes (em quilos) pescado no dia.
#● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
#● Se o valor da multa retornado for maior que zero, mostre a multa.
#● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa apagar."
#● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
#o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.

# Função que calcula a multa
def calcular_multa(peso_total):
    limite = 100
    if peso_total > limite:
        excesso = peso_total - limite
        multa = excesso * 4.0
        return multa
    else:
        return 0.0

# Programa principal
total_multa = 0.0  # acumulador de multas

while True:
    peso = float(input("Digite o peso de peixes (em kg) ou 0 para encerrar: "))
    
    if peso == 0:
        break  # encerra o loop
    
    multa = calcular_multa(peso)  # chama a função
    
    if multa > 0:
        print(f"Peso acima do limite! Multa de R$ {multa:.2f}")
    else:
        print("Peso dentro do limite. Nenhuma multa a pagar.")
    
    total_multa += multa  # soma ao total

# Exibe o total de multas acumuladas
print(f"\nTotal de multa acumulada: R$ {total_multa:.2f}")