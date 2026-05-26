lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'me diga qual valor ficara na posicao {c+1}°: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        else:
            if lista[c] < menor:
                menor = lista[c]
print(f'todoso os valores digitados foram {lista}')
print(f'o maior numeri digitado foi {maior}')
print(f'o menor numero digitado foi {menor}')
