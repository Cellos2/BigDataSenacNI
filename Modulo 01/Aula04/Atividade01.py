#1. Cálculo de Lâmpadas:
#Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
#iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
#lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
#cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
#3m² existe um bocal para uma lâmpada

# Entrada de dados
potencia_lampada = float(input("Informe a potência da lâmpada (W): "))
largura = float(input("Informe a largura do cômodo (m): "))
comprimento = float(input("Informe o comprimento do cômodo (m): "))

# Cálculos
area = largura * comprimento
potencia_necessaria = area * 3
lampadas_necessarias = potencia_necessaria / potencia_lampada
bocais_disponiveis = area / 3

# Ajuste com if/elif
if lampadas_necessarias <= bocais_disponiveis:
    lampadas_finais = lampadas_necessarias
else:
    lampadas_finais = bocais_disponiveis

# Arredondar para cima (pois não dá para ter 0.5 lâmpada)
import math
lampadas_finais = math.ceil(lampadas_finais)

# Saída
print(f"\nÁrea do cômodo: {area:.2f} m²")
print(f"Potência total necessária: {potencia_necessaria:.2f} W")
print(f"Lâmpadas necessárias (limitadas pelos bocais): {lampadas_finais}")


