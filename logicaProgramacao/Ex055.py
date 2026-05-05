maior = 0
menor = 0
for p in range (1, 6):
     Peso = float(input(f'Digite o peso {p} da pessoa: '))
     if p == 1:
        maior = Peso
        menor = Peso
     else:
        if Peso > maior:
            maior = Peso
        if Peso < menor:
                menor = Peso
print(f"O maior peso foi {maior} e o menor peso foi {menor}")