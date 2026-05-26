alunos = dict()
alunos['nome'] = str(input('nome: '))
alunos['média'] = float(input(f'média de {alunos["nome"]}: '))
if alunos['média'] >= 7:
    alunos['situação'] = 'aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['situação'] = 'recuperação'
else:
    alunos['situação'] = 'reprovado'
for k, v in alunos.items():
    print(f'{k} é {v}')