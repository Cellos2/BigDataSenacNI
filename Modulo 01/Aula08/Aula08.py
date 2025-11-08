#Atividade Assistida
#Faça um código que possa ler 3 pares de números inteiros, calcular e imprimir a soma de
#cada par separadamente. Obrigatoriamente, devemos usar a função somar que acabamos
#de criar.
# 1. Definimos nossa ferramenta: a função de somar
def somar(a, b):
 """
 Esta função recebe dois números (a e b) e retorna a soma deles.
 (Isso é uma 'docstring', uma boa prática para documentar o que a função faz)
 """
 resultado = a + b
 return resultado
# 2. Parte principal do nosso programa
print("Calculadora de Somas")
# 3. Vamos usar um loop 'for' para tratar dos 3 pares
for i in range(3):
 print(f"\n--- Calculando {i+1}º par ---")
 
 # Pedimos os números ao usuário
 num1 = int(input("Digite o primeiro número: "))
 num2 = int(input("Digite o segundo número: "))
 
 # Chamamos a função com os números que o usuário digitou
 # e guardamos o valor que ela 'retornou'
 resultado_da_soma = somar(num1, num2)
 
 # Imprimimos o resultado
 print(f"A soma de {num1} + {num2} é = {resultado_da_soma}")
print("\nPrograma finalizado!")