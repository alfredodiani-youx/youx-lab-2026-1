numero = soma = 0
while True:
    numero= int(input('digite um numero'))
    if numero == 999:
        break
    soma += numero
print(f'a soma vale {soma}')