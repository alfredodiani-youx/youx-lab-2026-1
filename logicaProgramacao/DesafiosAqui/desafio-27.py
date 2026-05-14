from gettext import find
from os import name
from os.path import split

nome=str(input('digite seu nome completo: ')).strip()
nome_separado= nome.split()
print(nome_separado)
print('Seu primeiro nome é: {}'.format (nome_separado[0]))
print('Seu ultimo nome é: {}'.format(nome_separado[-1]))
