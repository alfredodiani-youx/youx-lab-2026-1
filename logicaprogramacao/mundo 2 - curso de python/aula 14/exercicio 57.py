sexo = str(input('Informe seu sexo: [m/f]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")