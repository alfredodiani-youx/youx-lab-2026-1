#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n1 = int(input("Digite um numero: "))
unidade = n1 // 1 % 10
dezena = n1 // 10 % 10
centena = n1 // 100 % 10
milhar = n1 // 1000 % 10
print("analisando...")
print(f"A unidade é {unidade}")
print(f"A centena é {centena}")
print(f"A dezena é {dezena}")
print(f"O milhar é {milhar} ")

