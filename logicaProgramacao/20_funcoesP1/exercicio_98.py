from time import sleep

def contador(a, b, c):
    if c == 0:
        c = 1
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    if a < b and c < 0:
        c = abs(c)
    if b > a and b > 0:
        b += 1
    if a > b > 0:
        b -= 1
    elif a > b < 0:
        b -= 1
    if b < a and c > 0:
        c *= -1
    for y in range(a, b, c):
        print(y, end=' ')
        sleep(0.3)
    print('FIM!')

# start program
contador(1, 10, 1)
contador(10, 1, -2)
print('-='*30)
print('AGORA É SUA VEZ!!')
valor1 = int(input('Inicio: '))
valor2 = int(input('Fim: '))
valor3 = int(input('Passo: '))
