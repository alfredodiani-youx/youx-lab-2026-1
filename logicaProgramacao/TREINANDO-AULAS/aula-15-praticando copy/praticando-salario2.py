salarios = []

for i in range(3):
    s = float(input('digite o salario: '))
    salarios.append(s)

for salario in salarios:
    print(salario * 1.20)

print('maior salario: ', max (salarios))
print('menor salario: ', min (salarios))
print('media: ', sum (salarios) / len(salarios))