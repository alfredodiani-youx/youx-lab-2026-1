from time import sleep


def maior(*valores):
    maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for n in valores:
        print(n, end=' ')
        print('', end='')
        sleep(0.25)
    print(f'Foram iformados {len(valores)} valores ao todo.')
    for i in valores:
        if i == 0:
            maior = i
        elif i > maior:
            maior = i
    print(f'O maior valor informado foi {maior}.')

maior(1, 3, 9, 2, 10)
maior(3, 1, 4, 8, 6)
maior(9, 14, 19, 5, 17)