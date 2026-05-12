#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
# digitar valor

cont = 0
maior = 0
soma = 0
r = ''
while "N" not in r:
    num = int(input("Digite um numero: "))
    menor = num
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    r = input("Voce quer continuar[S/N]: ").upper()
media = soma / cont
print(f"Voce digitou {cont} numeros e a media deles é {media} o maior numero é {maior} o menor é {menor}")