# listaNumeros = [2, 24, 200, 5]
# maior = 0
# menor = 0
#
# for i in listaNumeros:
#     # numero = int(input(f"Digite um número para a posição {i}: "))
#     # listaNumeros.append(numero)
#     if i == 0:
#         maior = numero
#         menor = numero
#     else:
#         if numero < menor:
#             menor = numero
#         if numero > maior:
#             maior = numero
#
# #printando o maior número e suas posição
# print(f"O maior número é {maior} nas posições ", end=' ')
#
# for indice, valor in enumerate(listaNumeros):
#     if maior == valor:
#         print(f" {indice} ... ",end='')
# print()
#
# print(f"O menor número é {menor} nas posiçãoes: ", end=' ')
# for indice, valor in enumerate(listaNumeros):
#     if menor == valor:
#         print(f' {indice} ...',end='')
# print()
# print(f"Você digitou os valores {listaNumeros}")

# lista = [2,65,87,9]
contador = 0
contadorN2 = 0
terceiro = 0
for i in range(4):
    numero = int(input("Digite um número: "))
    if contador == 0:
        contadorN2 += 1
    if contadorN2 == 3:
        terceiro = numero
print(terceiro)