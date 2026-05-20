# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
numero = 0
while numero >= 0:
    numero = int(input('Digite um número para ver sua tabuada: '))
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(numero, c, numero * c))
print('PROGAMA ENCERRADO! VOLTE SEMPRE! ')