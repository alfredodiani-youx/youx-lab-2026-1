nome = input('digite seu nome completo:')

maiusculo = nome.upper()
print(f'seu nome em maiusculo é {maiusculo}')

minusculo = nome.lower()
print(f'seu nome em minusculo é {minusculo}')

letras = len(nome)
print(f'seu nome {nome} tem {letras} letras')

espaço = nome.split()
primeiro = len(espaço)
print(f'seu primeiro nome é {espaço[0]} e ele tem {len(espaço[0])} letras ')