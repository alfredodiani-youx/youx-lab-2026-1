lista = list()
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        resposta = str(input('Deseja adicionar mais um? [S/N] ')).upper()
        if resposta in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resposta == 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.')
media = soma / len(lista)
print(f'- a média de idade é {media:5.2f} anos.')
print('- As mulheres cadastradas foram ', end='')
for pessoa in lista:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}', end='')
print()
print(f'- Lista das pessoas que estão acima da média: ')
for pessoa in lista:
    if pessoa['idade'] >= media:
        print('   ')
        for key, value in pessoa.items():
            print(f'{key} = {value}', end='')
            print()
print('<< ENCERRADO >>')
