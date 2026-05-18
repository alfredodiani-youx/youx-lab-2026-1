lista = []

for contagem in range(0, 5):
    numero = int(input('digite um valor: '))
    if contagem == 0 or numero > lista[-1]:
        lista.append(numero)

    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
            posicao += 1

print(f'os valores digitados em ordem foram {lista}')
