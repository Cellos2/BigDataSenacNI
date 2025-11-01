#5. Média do Aluno com Optativa:
#Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
#optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
#ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
#substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
#mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:
#Aprovado: média >= 6.0
#Reprovado: média < 3.0
#Recuperação: média >= 3.0 e < 6.0
#Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
#resultado final.

# Leitura das notas
n1 = float(input("Digite a nota da 1ª avaliação: "))
n2 = float(input("Digite a nota da 2ª avaliação: "))
optativa = float(input("Digite a nota da prova optativa (ou -1 se não fez): "))

# Substituição se o aluno fez a optativa
if optativa != -1:
    if n1 < n2:
        n1 = optativa  # substitui a menor
    else:
        n2 = optativa

# Cálculo da média
media = (n1 + n2) / 2

# Classificação do aluno
if media >= 6.0:
    print(f"Média: {media:.2f} — Aluno APROVADO ")
elif media >= 3.0:
    print(f"Média: {media:.2f} — Aluno em RECUPERAÇÃO ")
else:
    print(f"Média: {media:.2f} — Aluno REPROVADO ")