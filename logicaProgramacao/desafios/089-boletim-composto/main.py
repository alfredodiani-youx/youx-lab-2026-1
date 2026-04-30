dados = list()
continuar = "S"
while continuar == "S":
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    continuar = str(input("Deseja  continuar? [S/N] ")).upper()
    while continuar not in 'NS':
        print('Resposta inválida. Tente novamente')
        continuar = str(input("Deseja  continuar? [S/N] ")).upper()
print('-='*30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*26)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
aluno = 1
while aluno != 999:
        print('-'*35)
        aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if aluno == 999:
            print('FINALIZANDO...')
        if aluno <= len(dados) - 1:
            print(f'Notas de {dados[aluno][0]} são {dados[aluno][1]}')
print('<<< VOLTE SEMPRE >>>')