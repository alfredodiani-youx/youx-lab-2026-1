salario = float(input('Digite o salário R$:'))
if salario >= 1250:
    salario = (salario*0.10)+salario
    print(f'O seu salário passou a ser R${salario:.2f}')
else:
    salario = (salario*0.15)+salario
    print(f'O seu salário passou a ser R${salario:.2f}')