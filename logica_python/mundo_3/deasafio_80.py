
#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
#uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

list = []
for c in range (0, 5):
    n = int(input('digite um valor:'))
    if c == 0 or n > list [-1]:
        list.append(n)
        print('adicionado ao final da lista...')
else:
    pos = 0
    while pos < len(list):
        if n <= list[pos]:
            list.insert(pos, n)
            print(f'adiciondo na posicao {pos} da lista...')
            break
        pos += 1
print('-=' * 30)
print(f'os valores digitados em ordem foram [list')
