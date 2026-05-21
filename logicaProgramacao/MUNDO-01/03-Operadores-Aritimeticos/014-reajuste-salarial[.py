salario = float(input('qual e o salario do funcionario? '))
NVS = input('nome do funcionario?')
novo = salario + (salario * 15 / 100)
print('o {} recebia {:.2f}, com 15% de aumento, passa a receber {:.2f}'.format(NVS, salario, novo))