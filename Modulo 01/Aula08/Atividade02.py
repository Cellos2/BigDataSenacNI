#2. Calculadora de IMC
#Crie um programa que leia a altura e o peso de N pessoas (pergunte ao usuário quantas
#pessoas são). Para cada pessoa, mostre seu IMC e a classificação.
#● Fórmula: IMC = PESO / (ALTURA * ALTURA)
#● Obrigatório (Função 1): Crie uma função calcular_imc(peso, altura) que receberá
#os valores e retornará o IMC calculado.
#● Obrigatório (Função 2): Crie outra função obter_classificacao(imc) que recebe o
#valor do IMC (calculado pela função 1) e retorna uma string com a classificação.
#○ Valores de Referência:
#■ Menor que 18.5: "Abaixo do peso"
#■ 18.5 a 24.9: "Peso normal"
#■ 25.0 a 29.9: "Sobrepeso"
#■ 30.0 ou mais: "Obesidade"
#● O programa principal deve pedir N, fazer um loop N vezes, pedir peso e altura, chamar as duas funções e imprimir o resultado formatado.

# Função 1 – Calcula o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

# Função 2 – Retorna a classificação do IMC
def obter_classificacao(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Programa principal
n = int(input("Quantas pessoas deseja avaliar? "))

for i in range(1, n + 1):
    print(f"\n--- Pessoa {i} ---")
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    imc = calcular_imc(peso, altura)
    classificacao = obter_classificacao(imc)

    print(f"IMC: {imc:.2f} — Classificação: {classificacao}")

print("\nCálculo finalizado para todas as pessoas.")
