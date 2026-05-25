lista_numero = []

for numero in range(0, 5):
    numero = int(input('Digite um valor: '))
    lista_numero.append(numero)
maior = max(lista_numero)
menor = min(lista_numero)
print(f'o maior número é {maior} que está na posição {lista_numero.index(maior)} e o menor é {menor} que esta na menor posição {lista_numero.index(menor)} ')