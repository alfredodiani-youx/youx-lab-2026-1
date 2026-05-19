#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

numeros= list()
pares= list()
impares= list()
while True:
    numeros.append(int(input('digite um numero')))
    resposta= str(input("deseja continur? [s/n]"))
    if resposta in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'a lista normal é {numeros}')
print(f'a lista de numeros pares é {pares}')
print(f'a lista denumeros impares é {impares}')