#3. Conversor de Temperatura
#Crie um programa que permita ao usuário converter temperaturas entre Celsius e
#Fahrenheit.
#● Função 1: Crie uma função celsius_para_fahrenheit(temp_c) que recebe a
#temperatura em Celsius e retorna o valor em Fahrenheit.
#○ Fórmula: F = (C * 9/5) + 32
#● Função 2: Crie uma função fahrenheit_para_celsius(temp_f) que recebe a
#temperatura em Fahrenheit e retorna o valor em Celsius.
#○ Fórmula: C = (F - 32) * 5/9
#● O programa principal deve perguntar ao usuário qual conversão ele quer fazer (ex:
#"1 para C->F" ou "2 para F->C"), pedir o valor, chamar a função correta e mostrar o
#resultado.
#Desafio: Criar uma única função que faça qualquer uma das conversões,
#sempre perguntando ao usuário qual é desejada.

def converter_temperatura():
    print("Conversor de Temperatura")
    print("1 - Celsius → Fahrenheit")
    print("2 - Fahrenheit → Celsius")

    opcao = input("Escolha a opção (1 ou 2): ")

    if opcao == "1":
        temp_c = float(input("Digite a temperatura em °C: "))
        temp_f = (temp_c * 9/5) + 32
        print(f"{temp_c:.2f}°C = {temp_f:.2f}°F")

    elif opcao == "2":
        temp_f = float(input("Digite a temperatura em °F: "))
        temp_c = (temp_f - 32) * 5/9
        print(f"{temp_f:.2f}°F = {temp_c:.2f}°C")

    else:
        print("Opção inválida! Escolha 1 ou 2.")

# Programa principal
converter_temperatura()