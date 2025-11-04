# # 3. Tentativa de Login e Senha. Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
# para digitar a senha correta.
#   ● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
#   ● Dê ao usuário 3 tentativas para acertar a combinação.
#   ● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
#   break para sair do loop.
#   ● Se a senha estiver errada, informe o erro e diminua o número de tentativas restantes.
#   ● Se as tentativas acabarem, imprima uma mensagem de bloqueio.

# Definindo usuário e senha corretos
usuario_correto = "admin"
senha_correta = "123456"

# Número máximo de tentativas
tentativas_restantes = 3

while tentativas_restantes > 0:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verifica se está correto
    if usuario == usuario_correto and senha == senha_correta:
        print("✅ Login realizado com sucesso! Bem-vindo!")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"❌ Usuário ou senha incorretos. Você ainda tem {tentativas_restantes} tentativa(s).")
        else:
            print("🚫 Tentativas esgotadas. Usuário bloqueado!")