numero = soma = cont = 0
while True:
    numero = int(input('Digite um numero [999/Stop]: '))
    print('-=-' * 10)
    if numero == 999:
        break
    cont += 1
    soma += numero
print('-=-' * 10)
print(f'Foram Digitados {cont} numeros e a soma foi {soma} ')