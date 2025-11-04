#1. Cálculo de Média Escolar para Vários Alunos
#Use o laço for para repetir a lógica de cálculo de média e status
#(Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes


for i in range(1, 11):  # repete de 1 até 10 (10 alunos)
    print(f"\n--- Aluno {i} ---")

    # Entrada de notas
    n1 = float(input("Digite a nota da 1ª avaliação: "))
    n2 = float(input("Digite a nota da 2ª avaliação: "))
    optativa = float(input("Digite a nota da prova optativa (ou -1 se não fez): "))

    # Substituição da menor nota, se houver optativa
    if optativa != -1:
        if n1 < n2:
            n1 = optativa
        else:
            n2 = optativa

    # Cálculo da média
    media = (n1 + n2) / 2

    # Classificação do aluno
    if media >= 6.0:
        print(f"Média: {media:.2f} — Aluno APROVADO")
    elif media >= 3.0:
        print(f"Média: {media:.2f} — Aluno em RECUPERAÇÃO")
    else:
        print(f"Média: {media:.2f} — Aluno REPROVADO")