from datetime import datetime
dados = dict()
dados['nome'] =str(input('nome: '))
nascimento = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['carteira de trabalho'] =int(input('carteira de trabalho (0 se nao tem): '))
if dados['carteira de trabalho'] != 0:
    dados['contratação'] =int(input('ano de contratação: '))
    dados['salário'] =float(input('qual salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'- {k} tem o valor de {v}')