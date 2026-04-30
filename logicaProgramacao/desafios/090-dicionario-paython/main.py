dados = {}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados['nome']}: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Reprovado'
print('-'*30)
for k, v in dados.items():
    print(f'  - {k} é igual a {v}')