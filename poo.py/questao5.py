def montar_tabela():
    print("Tabela de Preços - Loja da Sra. Amanda")
    print("--------------------------------------------")
    for quantidade in range(1, 51):
        preco = quantidade * 1.99
        print(f"{quantidade} itens - R$ {preco:.2f}")

def calcular_valor(qtd_itens):
    if 1 <= qtd_itens <= 50:
        valor = qtd_itens * 1.99
        print(f"Total para {qtd_itens} itens: R$ {valor:.2f}")
    else:
        print("Quantidade fora da tabela. Insira um valor entre 1 e 50.")

montar_tabela()

qtd_itens = int(input("\nInsira a quantidade de itens para calcular o valor: "))
calcular_valor(qtd_itens)
