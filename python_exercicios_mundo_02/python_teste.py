#nome = str(input("Qual é o seu nome? "))
#if nome == "helena":
    #print("Que lindo nome")
#print("tenha um bom dia {}".format(nome))


#nome = str(input("Qual é o seu nome? "))
#if nome == ("Helena"):
    #print("Que nome bonito vc tem!")
#elif nome == "João" or nome == "Alfredo" or nome == "Paim":
    #print("Seu nome é bem comum!")
#else:
    #print("nome legal")
#print("tenha um bom dia,{}".format(nome))


#Escreva um programa para aprovar o empréstimo bancário para a
#compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = str(input("Qual o valor da casa? "))
salario = str(input("Qual é o seu salario? "))
anos = str(input("Em quantos anos vc vai pagar? "))
prestacao = valor / (anos * 12)
PorCentoSalario = salario * 0.30
if prestacao > PorCentoSalario:
    print("Empréstimo NEGADO")
else:
    print("Empréstimo APROVADO")
