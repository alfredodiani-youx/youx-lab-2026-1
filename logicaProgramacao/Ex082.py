numero = list()
pares = list()
impares = list()
continuacao = 'S'
while True:
    print('-=-' * 10)
    numero.append(int(input("Digite um número: ")))
    print('Valor adicionado com sucesso...')
    continuacao = str(input('Deseja Continuar? [S/N]: ')).upper().strip()

    if continuacao in 'Nn':
        break

for indice,v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)

    elif v % 2 == 1:
        impares.append(v)

print('-=-' * 10)
print(f'A lista dos numeros e {numero}')
print(f'A lista dos pares e {pares}')
print(f'A lista dos impares e {impares}')