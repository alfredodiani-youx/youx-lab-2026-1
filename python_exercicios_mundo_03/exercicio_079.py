#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = []
continuar = "S"
while continuar != "N":
    numero = int(input("Digite um número: "))
    if numero in lista:
        print("Número não adicionado, pois ele já exite na lista. ")
    else:
        lista.append(numero)
    continuar = str(input("Quer continuar? [S/N] ")).upper()

print(lista)
