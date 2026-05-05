salario = float(input('qual o salario? $'))
if salario >= 1250:
  novo = salario + (salario * 15 / 100 )
else:
  novo = salario + (salario * 10 / 100)
print(f'quando ganhava ${salario} vai pasar a ganhar {novo}')