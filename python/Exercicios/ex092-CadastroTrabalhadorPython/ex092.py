from datetime import datetime
import math
dados = dict()
dados['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - anoNascimento
dados['ctps'] = int(input('Carteira de Trabalho (se não tiver, digite 0): '))
if dados['ctps'] != 0:
    dados['contr'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contr'] + 35)- datetime.now().year)
print('-='*20)
print(dados)
for key, valor in dados.items():
    print(f'{key} tem valor de {valor}')