numero = cont = soma = 0
numero = int(input('Digite um número [999 para parar]: '))

while True:
    cont += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
print(f'Você digitou {cont} números e a soma entre eles é {soma}')