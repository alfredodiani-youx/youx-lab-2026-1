#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

lista_numerica = []

for n in range (0, 5+1):
    valor = int(input("Digite um valor: "))
    if n == 0 or n > lista_numerica[-1]:
        lista_numerica.append(valor)
        print("Valor adiocionado ao final da lista")
    else:
        pos = 0
        while pos < len(lista_numerica):
            if valor <=lista_numerica[pos]:
                pos += 1
                lista_numerica.append(valor)
                lista_numerica.append(pos)
                print(f"O valor {valor} adicionado na posicao {pos} ")