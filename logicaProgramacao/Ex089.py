continuar = 'S'
dados = []
while continuar == 'S':
    print('-='*28)
    nome = (str(input('Digite o nome do aluno: ')))
    nota1 = (int(input('Nota 1: ')))
    nota2 = (int(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    dados.append([nome,[nota1,nota2],media])
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if continuar == 'N':
        print(f'{"No.":<4} {"Nome":<10} {"Media":<8}')
        for i, aluno in enumerate(dados):
            print(f'{i:<4} {aluno[0]:<10} {aluno[2]:<8}')
        print('-=' * 28)
opcao = ''
while opcao != '999':
    print('-=' * 28)
    opcao = int(input('Mostrar nota do aluno [999/STOP]: '))
    if opcao <= len(dados) -1:
        print(f' As notas de {dados[opcao][0]} foram {dados[opcao][1]} ')