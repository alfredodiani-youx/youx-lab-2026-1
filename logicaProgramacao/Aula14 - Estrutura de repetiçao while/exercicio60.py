#Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input("Digite um numero para calcular seu fatorial: "))
c = num
f = 1
while c > 0:
    print(f"{c}", end= '')
    print(f" x " if c > 1 else ' = ', end= '')
    f *= c
    c -= 1
print(f"{f} ")