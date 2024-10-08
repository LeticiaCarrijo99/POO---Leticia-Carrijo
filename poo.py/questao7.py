def calcular_divida(valor_divida):
    opcoes_pagamento = { 
        1: 0,     
        3: 0.10,  
        6: 0.15,  
        9: 0.20,  
        12: 0.25  
    }

    print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
    print("------------------------------------------------------------------------------")

    for parcelas, juros in opcoes_pagamento.items():
        valor_juros = valor_divida * juros
        valor_total = valor_divida + valor_juros
        valor_parcela = valor_total / parcelas
        print(f" R$  {valor_total:12.2f} | {juros * 100:14.2f}% | {parcelas:^21} | R$ {valor_parcela:13.2f}")

valor_divida = float(input("Digite o valor da dívida: R$ "))
calcular_divida(valor_divida)
