#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final,
# mostre quantos números foram digitados
# e qual foi a soma entre elas (desconsiderando o flag).

contador = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input('digite um valor (digite 999 pra parar): '))
    soma += numero
    contador += 1
print(f'a soma dos valores foi {soma-999}')
print(f"Voce digitou {contador-1} numeros")