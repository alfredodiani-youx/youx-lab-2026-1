#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um numero: "))
for c in range (1 , num +1 ):
    if num % c:
        print("\033[33m", end= '')
    else:
        print("\033[31m", end= '')
    print(f" {c} ", end= '')
