cont = 1
soma = 0
while True:
    pessoa = int(input('Digite seu numero (999 para parar): '))
    if pessoa == 999:
        break
    else:
        soma += pessoa
        cont += 1
print(f'Voce digitou {cont} numeros e a soma deles e {soma}')

