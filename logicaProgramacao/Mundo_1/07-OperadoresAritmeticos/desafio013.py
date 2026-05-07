#REAJUSTE SALARIAL
#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

salario = float(input('Qual é o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
