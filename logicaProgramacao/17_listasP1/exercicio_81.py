#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista= []
while True:
    lista.append(int(input("digite um valor :")))
    resposta= str(input("voce deseja continuar? [s/n]"))
    if resposta in 'Nn':
        break
print(f'foram digitados {len(lista)} a lista')
lista.sort(reverse=True)
print(f'os valores em ordem crescente sao {lista}')
if 5 in lista:
    print('o valor 5 faz parte da lista')
else:
    print("o valor 5 nao faz parte da lista")