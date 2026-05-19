from random import randint
lista = list()
quantidade = int(input('Quantos jogos voce quer fazer? '))
total = 1
jogos = list()
while total <= quantidade:
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Os numeros sorteados foram {jogos}')
