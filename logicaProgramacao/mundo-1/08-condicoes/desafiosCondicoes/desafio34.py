salario = float(input('Qual seu salario? '))
if salario > 1250:
    print(f'Seu salario sera R${salario + (salario / 10)}')
else:
    print(f'Seu salario sera R${salario + (salario * 15/100):.2f}')