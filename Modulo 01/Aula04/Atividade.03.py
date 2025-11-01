#3. Rendimento do Taxista:
#Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
#preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
#odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
#combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
#média do consumo em km/L e o lucro (líquido) do dia.

# Entrada de dados
inicio = float(input("Marcação do odômetro no início do dia (km): "))
fim = float(input("Marcação do odômetro no final do dia (km): "))
litros = float(input("Quantidade de litros gastos: "))
valor_recebido = float(input("Valor total recebido (R$): "))

# Preço do combustível
preco_combustivel = 6.15

# Cálculos básicos
distancia = fim - inicio
media = distancia / litros
custo = litros * preco_combustivel
lucro = valor_recebido - custo

# Estrutura condicional
if lucro > 0:
    print("Lucro positivo! O taxista teve um bom dia de trabalho. 💰")
    print("Lucro líquido: R$", round(lucro, 2))
    print("Média de consumo:", round(media, 2), "km/L")
elif lucro == 0:
    print("Sem lucro nem prejuízo. O rendimento ficou no ponto de equilíbrio.")
    print("Média de consumo:", round(media, 2), "km/L")
else:
    print("Lucro negativo! Houve prejuízo no dia. 🚨")
    print("Prejuízo de: R$", round(abs(lucro), 2))
    print("Média de consumo:", round(media, 2), "km/L")
