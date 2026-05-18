#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#o programa será interrompido quando o número solicitado for negativo.

contagem = 0
while True:
    numero = int(input('digite um numero para ver sua tabuada: '))
    if numero >= 0:
        for contagem in range(1,11):
            if contagem  <= 10:
                print(f'{numero} x {contagem} = {numero*contagem}')
    else:
        print('numero INVALIDO')
        break

print('FIM')



