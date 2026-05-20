
#Exercício Python 066: Crie um programa que leia números inteiros pelo
#teclado. O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final,
#mostre quantos números foram digitados e qual foi a soma entre elas (desconsider

numero = soma = quantidade = 0
while numero != 999:
    quantidade += 1
    numero = int(input('Digite um número: [999 para parar] '))
    if numero != 999:
        soma += numero
print(f'a soma dos {quantidade-1} números foi {soma}')