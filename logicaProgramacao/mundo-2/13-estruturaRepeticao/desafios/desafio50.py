soma = 0
count = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° numero: '))
    if num % 2 == 0:
        soma += num
        count += 1
print(f'Voce digito {count} numeros pares e a soma deles e {soma}')