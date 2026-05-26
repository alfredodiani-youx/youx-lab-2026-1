def contador(i,f,p):
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ')
            cont -= p
        print('FIM!')

contador(1,10,1)
contador(10,0,2)


numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite o outro numero numero: '))
numero3 = int(input('Digite de quanto em quanto: '))
contador(numero1,numero2,numero3)
