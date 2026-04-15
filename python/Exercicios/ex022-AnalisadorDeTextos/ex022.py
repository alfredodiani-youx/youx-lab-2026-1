nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

#Pode usar esses dois jeitos:
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separacao = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separacao[0], len(separacao[0])))

