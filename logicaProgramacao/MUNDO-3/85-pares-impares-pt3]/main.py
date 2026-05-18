pares = []
impares = []
lista = []
for contagem in range(0, 4):
    valor = int(input(f"Digite o {contagem+1}° valor: "))
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 != 0:
        impares.append(valor)
lista.append(pares)
lista.append(impares)
print(lista)
print(f"Os valores pares foram: {lista[0]}")
print(f"Os valores ímpares foram: {lista[1]}")