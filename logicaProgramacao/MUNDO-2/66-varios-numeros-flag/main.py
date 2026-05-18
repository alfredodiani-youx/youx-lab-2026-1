valor = 0
numero = 0
soma = 0
while True:
    valor += 1
    numero = int(input('digite um numero: '))
    if numero == 999:
        break
    soma += numero
print(f'a soma dos {valor} valores vale {soma}')
