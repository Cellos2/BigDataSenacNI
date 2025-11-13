# --- Tanoshimi: fluxo completo com mesa, garçom e caixa + mensagem final ---

MESAS   = ["M1", "M2", "M3", "Varanda-01", "Tatame-02"]
GARCONS = ["Bruno", "Carla", "João", "Mika", "Yumi"]
CARDAPIO = [
    ["1", "Sushi Combo (10 peças)", 35.00],
    ["2", "Temaki de Salmão",       25.00],
    ["3", "Yakisoba",               30.00],
    ["4", "Guioza (6 unid.)",       18.00],
    ["5", "Refrigerante",            8.00],
]

pedidos = {}
proximo_numero = 1

# ---------- Utilidades ----------
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
                return input("Digite o nome: ").strip()
        except ValueError:
            pass
        print("⚠️ Opção inválida. Tente novamente.")

def adicionar_itens():
    itens = []
    while True:
        mostrar_cardapio()
        cod = input("Código do item (0 para finalizar): ").strip()
        if cod == "0":
            break
        item = next((it for it in CARDAPIO if it[0] == cod), None)
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

def total_itens(itens):
    return sum(preco*qtd for _, _, preco, qtd in itens)

def imprimir_comprovante(p):
    print("\n======= COMPROVANTE =======")
    print(f"Pedido nº: {p['numero']}")
    print(f"Mesa: {p['mesa']} | Garçom: {p['garcom']}")
    print(f"Status: {p['status']}")
    print("---------------------------")
    for _, nome, preco, qtd in p["itens"]:
        print(f"{nome:28} x{qtd:<2}  R$ {(preco*qtd):>6.2f}")
    print("---------------------------")
    print(f"TOTAL: R$ {p['total']:.2f}")
    print("===========================\n")

# ---------- 1) Garçom registra pedido ----------
def registrar_pedido():
    global proximo_numero
    mesa = escolher_da_lista("Escolha a MESA:", MESAS)
    garcom = escolher_da_lista("Escolha o GARÇOM:", GARCONS)
    itens = adicionar_itens()
    if not itens:
        print("Pedido cancelado (sem itens).\n")
        return
    total = total_itens(itens)

    numero = proximo_numero
    proximo_numero += 1
    pedidos[numero] = {
        "numero": numero,
        "mesa": mesa,
        "garcom": garcom,
        "itens": itens,
        "total": total,
        "status": "ABERTO"
    }

    imprimir_comprovante(pedidos[numero])
    print(f"👉 Entregar ao cliente o CARTÃO com o número: {numero}\n")

# ---------- 2) Caixa recebe pagamento ----------
def caixa_pagamento():
    try:
        num = int(input("\nNúmero do pedido para pagamento: "))
    except ValueError:
        print("⚠️ Número inválido.")
        return

    p = pedidos.get(num)
    if not p:
        print("⚠️ Pedido não encontrado.")
        return
    if p["status"] == "PAGO":
        print("ℹ️ Este pedido já foi pago.")
        return

    imprimir_comprovante(p)

    taxa = input("Aplicar taxa de serviço 10%? (s/n): ").strip().lower()
    total_final = p["total"] * (1.10 if taxa == "s" else 1.00)

    print(f"Total a pagar: R$ {total_final:.2f}")
    print("Formas: 1-Dinheiro  2-Débito  3-Crédito  4-Pix")
    try:
        opc = int(input("Escolha a forma de pagamento: "))
    except ValueError:
        print("⚠️ Opção inválida.")
        return

    match opc:
        case 1: forma = "Dinheiro"
        case 2: forma = "Débito"
        case 3: forma = "Crédito"
        case 4: forma = "Pix"
        case _: 
            print("⚠️ Forma inválida.")
            return

    p["status"] = "PAGO"
    p["total_pago"] = total_final
    p["forma_pagto"] = forma

    print(f"\n✅ Pagamento confirmado! Pedido {p['numero']} — {forma} — R$ {total_final:.2f}")
    print("🧾 Obrigado e volte sempre!\n")

    # 💬 MENSAGEM FINAL DE ATENDIMENTO
    print("✨ Agradecemos por visitar o Restaurante Japonês Tanoshimi! ✨")
    print("🍣 Esperamos que tenha desfrutado de uma excelente experiência gastronômica.")
    print("🥢 Até a próxima visita, arigatô gozaimashita! 🙏\n")

# ---------- Menu principal ----------
def main():
    print("Bem-vindo ao Tanoshimi 🍣")
    while True:
        print("\n=== MENU ===")
        print("1. Garçom - Registrar pedido")
        print("2. Caixa  - Receber pagamento")
        print("3. Listar pedidos (relatório)")
        print("0. Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            registrar_pedido()
        elif op == "2":
            caixa_pagamento()
        elif op == "3":
            for p in pedidos.values():
                print(f"#{p['numero']} | Mesa {p['mesa']} | {p['garcom']} | {p['status']} | R$ {p['total']:.2f}")
        elif op == "0":
            print("\nEncerrando o sistema... até logo! 👋")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()