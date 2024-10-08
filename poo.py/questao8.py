def verificar_respostas(respostas_aluno, gabarito):
    acertos = 0
    for i in range(10):
        if respostas_aluno[i].upper() == gabarito[i]:
            acertos += 1
    return acertos

def main():
    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    maior_acerto = 0
    menor_acerto = 10
    total_alunos = 0
    soma_notas = 0
    continuar = 'S'

    while continuar.upper() == 'S':
        respostas_aluno = []
        print("\nDigite as respostas do aluno (A, B, C, D ou E):")
        for i in range(10):
            resposta = input(f"Resposta da questão {i+1}: ").upper()
            while resposta not in ['A', 'B', 'C', 'D', 'E']:
                resposta = input(f"Resposta inválida. Resposta da questão {i+1}: ").upper()
            respostas_aluno.append(resposta)

       
        acertos = verificar_respostas(respostas_aluno, gabarito)
        print(f"O aluno acertou {acertos} questões.")
        
        
        total_alunos += 1
        soma_notas += acertos
        if acertos > maior_acerto:
            maior_acerto = acertos
        if acertos < menor_acerto:
            menor_acerto = acertos

    
        continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").upper()


    if total_alunos > 0:
        media_notas = soma_notas / total_alunos
        print("\n--- Resumo Final ---")
        print(f"Maior acerto: {maior_acerto}")
        print(f"Menor acerto: {menor_acerto}")
        print(f"Total de alunos que utilizaram o sistema: {total_alunos}")
        print(f"Média das notas da turma: {media_notas:.2f}")
    else:
        print("Nenhum aluno utilizou o sistema.")

if __name__ == "__main__":
    main()
