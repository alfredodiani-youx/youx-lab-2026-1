#Escreva um programa para aprovar o empréstimo bancário para a
#compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual é o seu salario? "))
anos = float(input("Em quantos anos vc vai pagar? "))
prestacao = valor / (anos * 12)
PorCentoSalario = salario * 0.30
if prestacao > PorCentoSalario:
    print("Empréstimo NEGADO")
else:
    print("Empréstimo APROVADO")
