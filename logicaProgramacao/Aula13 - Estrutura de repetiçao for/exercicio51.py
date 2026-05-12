#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print("10 TERMOS DE UMA PA")
num = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo = num + (10 - 1) * razao
for t in range (num , decimo , razao):
    print(f'{t}', end= ' > ')
print("Acabou")