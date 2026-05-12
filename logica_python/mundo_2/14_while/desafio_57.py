sexo = str((input('digit o sexo: [F/M]'))).strip()[0]
while sexo not in 'MmFf':
    sexo = str((input('digit o sexo: [F/M]'))).strip()[0]
print(f'sexo {sexo} registrado com sucesso')
