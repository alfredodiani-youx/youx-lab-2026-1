sexo= str(input('Informe seu sexo [F/M]: '))
while sexo not in 'MmFf':
    r = str(input('Dados invalidos. Por favor informe seu sexo: [F/M] ')).upper()
print('Dados validos')