#4. Código de Origem do Produto:
#Escreva um programa que leia o código de origem de um produto e imprima na tela a região
#de sua procedência, conforme a tabela abaixo:
#Observação: caso o código não seja nenhum dos especificados, o produto deve ser
#encarado como “Importado”.

codigo = int(input("Digite o código de origem do produto: "))

if codigo == 1:
    print("Procedência: Sul")
elif codigo == 2:
    print("Procedência: Norte")
elif codigo == 3:
    print("Procedência: Leste")
elif codigo == 4:
    print("Procedência: Oeste")
elif codigo == 5 or codigo == 6:
    print("Procedência: Nordeste")
elif codigo >= 7 and codigo <= 9:
    print("Procedência: Sudeste")
else:
    print("Procedência: Importado")