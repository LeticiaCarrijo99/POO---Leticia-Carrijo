salario_inicial = 1000.00
ano_contratacao = 1995
ano_atual = 2025

aumento = 0.015  
salario = salario_inicial + (salario_inicial * aumento)

for ano in range(1997, ano_atual + 1):
    aumento *= 2  
    salario += salario * aumento 

print(f"O salário do funcionário em {ano_atual} será de R$ {salario:.2f}")
