#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for n in range (1 , 5 +1):
   num = int(input("Digite um numero(apenas a soma dos numeros pares sera mostrada): "))
   if num % 2 == 0:
      soma += num
      cont += 1
print(f"VOce informou {cont} numeros pares e a soma de todos esses numeros é {soma}")