maior = menor = 0
for c in range(0,5):
    peso = int(input(f'Peso {c+1}: '))
    if peso < 0:
        print('Peso inválido. Tente novamente.')
        peso = int(input(f'Peso {c + 1}: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior e {maior}kg e o menor e {menor}kg')