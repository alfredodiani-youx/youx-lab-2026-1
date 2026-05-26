nome = []
peso = []
quantidade = 0
maior = 0
menor = 0
while True:
    nome.append(str(input('nome: ')))
    quantidade = quantidade + 1
    peso.append(int(input('peso: ')))
    resposta =str(input('quer continuar [S/N]: ')).upper()
    if resposta == 'S':
        nome.append(str(input('nome: ')))
        peso.append(int(input('peso: ')))
        resposta = str(input('quer continuar [S/N]: '))
    elif resposta != 'S':
        break
print(f'ao todo voce cadastrou {quantidade} pessoas')