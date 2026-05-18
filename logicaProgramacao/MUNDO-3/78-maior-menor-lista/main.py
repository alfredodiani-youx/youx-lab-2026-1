lista = []

for i in range(0, 4):
    lista.append(int(input('digite um valor:  ')))
print(f'voce digitou os valores {lista}')

maior = ""
menor = ""

for i, e in enumerate(lista):
    if e == max(lista):
        maior += f"{i} "

    elif e == min(lista):
        menor += f"{i} "

print(f'o maior valor digitado foi {max(lista)} e ele aparece nas posiçoes {maior}')
print(f'o menor valor digitado foi {min(lista)} e ele aparece nas posiçoes {menor}')