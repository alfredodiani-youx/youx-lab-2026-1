soma = cont = 0
while True:
    num =int(input('digite um numero (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'a soma dos {cont} valores foi de {soma}')