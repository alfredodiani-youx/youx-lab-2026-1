#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o
# número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

numero= list()
while True:
    valor= int(input("digite um valor :"))
    if valor not in numero:
        numero.append(valor)
        print('o numero foi adicionado com sucesso')
    else:
        print('esse  valor já existe')
    resposta= str(input("voce deseja continuar?[s/n]"))
    if resposta in 'Nn':
        break
print(f'voce digitou os valores {numero}')
