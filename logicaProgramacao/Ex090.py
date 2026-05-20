dados = dict()
dados ['nome'] = str(input('Digite o nome do aluno (a): '))
dados['media'] = float(input(f'Digite a media de {dados ["nome"]}: '))
print('-='*10)
print(f'Nome e igual a {dados ["nome"]}')
print(f'Media e igual a {dados ['media']}')
if dados['media'] < 5.0:
    print(f'O Aluno(a) {dados ["nome"]} esta reprovado (a)!')
elif dados["media"] <= 7.0:
    print(f'O Aluno(a) {dados["nome"]} esta de recuperacao')
else:
    print(f'O Aluno(a) {dados["nome"]} esta aprovado (a)!')