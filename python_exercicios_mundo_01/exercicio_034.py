# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input('Quanto vc recebe? '))
if salario > 1250:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.15

print(f"O novo salario é {novo_salario}")
