#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.


reserva= []
principal= []
maior = menor = 0
while True:
    reserva.append(str(input('digite seu nome :')))
    reserva.append(str(input('digite seu peso :')))
    if len(principal) == 0:
        maior = menor = reserva[1]
    else:
        if reserva[1] > maior:
            maior = reserva[1]
        if reserva[1] < menor:
            menor = reserva[1]
    principal.append(reserva[:])
    reserva.clear()
    resposta= str(input("deseja continuar?[s/n] ?"))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'voce cadastrou {len(principal)} pessoas.')
print(f'o maior peso foi de {maior} kg')
for peso in principal:
    if peso[1] == maior:
        print(f'{peso[0]}')
print(f'o menor peso foi de {menor} kg')