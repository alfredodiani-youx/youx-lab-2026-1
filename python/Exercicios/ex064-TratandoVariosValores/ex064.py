numero = cont = soma = 0
numero = int(input('Digite o número [999 para parar]: '))

while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite o número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))
