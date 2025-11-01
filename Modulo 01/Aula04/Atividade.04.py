#4. Código de Origem do Produto:
#Escreva um programa que leia o código de origem de um produto e imprima na tela a região
#de sua procedência, conforme a tabela abaixo:
#Observação: caso o código não seja nenhum dos especificados, o produto deve ser
#encarado como “Importado”.

codigo = int(input("Digite o código de origem do produto: "))

match codigo:
    case 1:
        print("Região de origem: Sul")
    case 2:
        print("Região de origem: Norte")
    case 3:
        print("Região de origem: Leste")
    case 4:
        print("Região de origem: Oeste")
    case 5 | 6:
        print("Região de origem: Nordeste")
    case n if 7 <= n <= 9:
        print("Região de origem: Sudeste")
    case 10:
        print("Região de origem: Centro-Oeste")
    case 11:
        print("Região de origem: Noroeste")
    case _:
        print("Produto importado")
