def gerar_tabuada(numero):
    if 1 <= numero <= 10:
        for i in range(1, 11):
            print(f"{i} × {numero} = {i * numero}")
    else:
        print("Por favor, informe um número inteiro entre 1 e 10.")

numero = int(input("Informe um número entre 1 e 10 para gerar a tabuada: "))
gerar_tabuada(numero)