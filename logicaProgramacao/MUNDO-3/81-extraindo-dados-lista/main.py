lista = []
contagem = 0

while True:
    numero = int(input('digite um numero: '))
    opcao = input('quer continuar [S/N]')

    contagem += 1
    lista.append(numero)

    if opcao in 'Nn':
        break

print("=>"*30)

print(f'voce digitou {contagem} elementos')

lista.sort(reverse=True)

print(f'os valores em ordem decrescente sao: {lista}')

if 5 in lista:
    print('o numero 5 está presente na lista')


