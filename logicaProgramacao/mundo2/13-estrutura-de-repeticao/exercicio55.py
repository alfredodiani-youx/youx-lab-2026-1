peso = ''
maior = 0
for c in range(1,6):
    peso = float(input('qual é o seu peso?'))
    menor = peso
    maior = peso
    if peso > maior:
        maior = peso
    if menor < peso:
        menor = peso
print(f'o maior peso foi {maior} e o menor peso foi {menor}')
