from time import sleep

numero=int(input('Digite um número: '))
if numero==0 or numero==1:
    print('A sequência de Fibonacci é 0')
else:
    t1 = 0
    t2 = 1
    t3 = 0
    contador = 2
    while contador < numero:
        t3 = t1 + t2
        print(t3)
        t1 = t2
        t2 = t3
        contador += 1