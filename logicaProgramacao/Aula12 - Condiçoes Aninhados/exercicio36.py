#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
anos = int(input("Em quantos anos voce ira pagar? "))
minimo = salario * 30 / 100
prestacao_mensal = valor /  ( anos * 12)

if prestacao_mensal <= minimo:
    print ("Voce pode pagar ")
else:
    print("Emprestimo negado ")

