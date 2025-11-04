#2. Cadastro de Candidatos
#Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar candidatos menores de 18 anos:
#   ● O programa deve pedir o Ano de Nascimento do candidato.
#   ● Se for menor de 18, o programa deve informar que ele não pode participar e pular a coleta dos demais dados (telefone, email etc) para esse candidato.
#   ● Se for maior de 18, o programa prossegue com o input() para os demais dados

for candidato in range(12):
    try:
        print('Bem vindo(a) ao nosso processo seletivo, preencha os dados para sua candidatura!')
        print(f'\nCandidato {candidato + 1}:')
        ano_nascimento = int(input('Informe o ano do seu nascimento: '))
        ano_atual = 2025
        idade = ano_atual - ano_nascimento

        if idade < 18:
            print('Você tem menos de 18 anos. Não poderá participar da candidatura!')
            continue  # pula para o próximo candidato

        # Coleta os demais dados apenas se for maior de 18 anos
        nome = input('Informe seu nome completo: ')
        telefone = input('Informe seu telefone: ')
        email = input('Informe seu email: ')
        
        print(f'\nCadastro concluído com sucesso para {nome} ({idade} anos).')

    except ValueError:
        print('Por favor, insira um ano válido.')

        