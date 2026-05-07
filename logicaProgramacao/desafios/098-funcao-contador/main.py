from time import sleep

def contador(a, b, c):
    print('-='*30)
    if c < 0:
        c = c * -1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a > b:
        c = -c
    if c == 0:
        c = 1
    if b < a:
        b -= 1
    if b > a:
        b += 1
    for i in range(a, b, c):
        print(i, end=' ')
        print('', end='')
        sleep(0.5)
    print('FIM!')
    print('-=' * 30)


contador(1, 10, 1)
contador(10, 0, -2)
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
