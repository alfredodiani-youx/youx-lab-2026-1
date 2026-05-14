valores = []
resposta = 'S'
while resposta != 'n':
    valor = int(input('Digite seu valor: '))
    if valor not in valores:
        valores.append(valor)

    resposta = input('Voce deseja continuar? [S/N]').strip().lower()
print(f'a lista ordenada e: {sorted(valores)} ')
