#Crie um codigo que receba o salario de um funcionario e o mostre com 15% de aumento

salario = float(input("Digite o salario do funcionario para ser calculado o reajuste: R$"))
aumento = salario + (salario * 15 / 100 )
print(f"O atual salario do funcionario é R${salario:.2f} com o aumento de 15% o salario do funcionaria passara a ser R${aumento:.2f}")