def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

pares, impares = contar_pares_impares(numeros)

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
