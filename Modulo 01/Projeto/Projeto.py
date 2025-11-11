# --- Sistema Restaurante Japonês Tanoshimi (conta única por mesa) ---

MESAS = ["M1", "M2", "M3", "Varanda-01", "Tatame-02"]
GARCONS = ["Bruno", "Carla", "João", "Mika", "Yumi"]

CARDAPIO = [
    ["1", "Sushi Combo (10 peças)", 35.00],
    ["2", "Temaki de Salmão",       25.00],
    ["3", "Yakisoba",               30.00],
    ["4", "Guioza (6 unid.)",       18.00],
    ["5", "Refrigerante",            8.00],
]

def mostrar_cardapio():
    print("\n----- CARDÁPIO Tanoshimi -----")
    for cod, nome, preco in CARDAPIO:
        print(f"{cod} - {nome} - R$ {preco:.2f}")
    print("------------------------------")

def escolher_da_lista(titulo, opcoes):
    print(f"\n{titulo}")
    for i, item in enumerate(opcoes, start=1):
        print(f"{i}. {item}")
    print(f"{len(opcoes)+1}. Outro (digitar manualmente)")
    while True:
        try:
            pos = int(input("Selecione: "))
            if 1 <= pos <= len(opcoes):
                return opcoes[pos-1]
            elif pos == len(opcoes)+1:
                nome = input("Digite o nome: ").strip()
                if nome:
                    return nome
        except ValueError:
            pass
        print("⚠️ Opção inválida. Tente novamente.")

def adicionar_itens():
    itens = []
    while True:
        mostrar_cardapio()
        codigo = input("Código do item (0 para finalizar): ").strip()
        if codigo == "0":
            break
        item = next((it for it in CARDAPIO if it[0] == codigo), None)
        if not item:
            print("⚠️ Código inválido.")
            continue
        try:
            qtd = int(input(f"Quantidade de '{item[1]}': "))
            if qtd <= 0:
                print("⚠️ Informe quantidade positiva.")
                continue
        except ValueError:
            print("⚠️ Quantidade inválida.")
            continue
        itens.append([item[0], item[1], item[2], qtd])
    return itens

def calcular_total(itens):
    return sum(preco * qtd for _, _, preco, qtd in itens)

def gerar_comprovante_texto(pedido_num, mesa, garcom, itens, total, parcial=False):
    linhas = []
    titulo = "COMPROVANTE (PARCIAL)" if parcial else "COMPROVANTE DO PEDIDO"
    linhas.append("\n======= " + titulo + " =======")
    linhas.append(f"Pedido nº: {pedido_num}")
    linhas.append(f"Mesa: {mesa} | Garçom: {garcom}")
    linhas.append("-------------------------------------")
    for _, nome, preco, qtd in itens:
        subtotal = preco * qtd
        linhas.append(f"{nome:30} x{qtd:<2}  R$ {subtotal:>6.2f}")
    linhas.append("-------------------------------------")
    linhas.append(f"TOTAL: R$ {total:.2f}")
    linhas.append("=====================================\n")
    return "\n".join(linhas)

def main():
    pedidos_abertos = {}  # chave: mesa -> dict {numero, mesa, garcom, itens}
    historico_fechados = []
    proximo_numero = 1

    print("Bem-vindo ao Tanoshimi 🍣")
    while True:
        mesa = escolher_da_lista("Escolha a MESA:", MESAS)

        if mesa in pedidos_abertos:
            # Já existe conta aberta: vamos SOMAR itens no mesmo pedido
            pedido = pedidos_abertos[mesa]
            print(f"\n🔄 Mesa {mesa} já possui pedido aberto (nº {pedido['numero']}).")
            print(f"Garçom responsável: {pedido['garcom']}")
        else:
            # Criar novo pedido para a mesa
            garcom = escolher_da_lista("Escolha o GARÇOM:", GARCONS)
            pedido = {
                "numero": proximo_numero,
                "mesa": mesa,
                "garcom": garcom,
                "itens": []
            }
            pedidos_abertos[mesa] = pedido
            proximo_numero += 1
            print(f"\n🧾 Iniciado pedido nº {pedido['numero']} | Mesa: {mesa} | Garçom: {garcom}")

        # Adiciona novos itens (serão SOMADOS aos já existentes)
        novos = adicionar_itens()
        if not novos:
            print("Nenhum item informado. Nada foi alterado.\n")
        else:
            pedido["itens"].extend(novos)
            total = calcular_total(pedido["itens"])
            texto = gerar_comprovante_texto(pedido["numero"], mesa, pedido["garcom"], pedido["itens"], total, parcial=True)
            print(texto)
            input("Pressione Enter para continuar...")

        acao = input("Deseja finalizar a conta dessa mesa agora? (s/n): ").strip().lower()
        if acao == "s":
            total_final = calcular_total(pedido["itens"])
            cupom_final = gerar_comprovante_texto(pedido["numero"], mesa, pedido["garcom"], pedido["itens"], total_final, parcial=False)
            print(cupom_final)
            input("Pressione Enter para fechar...")
            historico_fechados.append({**pedido, "total": total_final, "cupom": cupom_final})
            del pedidos_abertos[mesa]

        continuar = input("Registrar/editar outro pedido? (s/n): ").strip().lower()
        if continuar != "s":
            break

    # Fechamento do turno
    if historico_fechados:
        faturado = sum(p["total"] for p in historico_fechados)
        print("\n--- RESUMO DO TURNO ---")
        print(f"Pedidos fechados: {len(historico_fechados)} | Faturado: R$ {faturado:.2f}")
        print("\n--- COMPROVANTES FECHADOS ---")
        for p in historico_fechados:
            print(p["cupom"])
    if pedidos_abertos:
        print("\n⚠️ Existem mesas ainda ABERTAS (não faturadas):")
        for mesa, p in pedidos_abertos.items():
            print(f"- Mesa {mesa} | Pedido {p['numero']} | Garçom {p['garcom']} | Itens: {len(p['itens'])}")
    print("\nObrigado por escolher o Tanoshimi! 🍱")

if __name__ == "__main__":
    main()