lista = []

while True:
    numero = int(input('digite um valor: '))
    if numero not in lista:
        lista.append(numero)
    opcao = input("deseja continuar S/N: ")
    if opcao not in "Ss":
        break
print(f'voce digitou os valores {lista}')