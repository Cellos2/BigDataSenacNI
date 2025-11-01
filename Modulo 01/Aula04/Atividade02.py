#2. Quantidade de Caixas de Azulejos:
#Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
#largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
#todas as suas paredes (considere que não será descontada a área ocupada por portas e
#janelas). Cada caixa de azulejos possui 1,5 m²

# Leitura dos dados
comprimento = float(input("Digite o comprimento da cozinha (m): "))
largura = float(input("Digite a largura da cozinha (m): "))
altura = float(input("Digite a altura da cozinha (m): "))

# Cálculo da área total das paredes
area_total = 2 * (comprimento * altura + largura * altura)

# Cada caixa cobre 1,5 m²
area_caixa = 1.5

# Cálculo da quantidade de caixas
divisao = area_total / area_caixa
resto = area_total % area_caixa

# Estrutura condicional
if resto == 0:
    caixas = int(divisao)
elif resto > 0:
    caixas = int(divisao) + 1
else:
    caixas = 0  # caso improvável, mas para garantir

# Exibição do resultado
print("Área total das paredes:", area_total, "m²")
print("Serão necessárias", caixas, "caixas de azulejos.")