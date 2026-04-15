#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Nome: ')
print(f'Nome verificado: {nome}')
print(f'Possui "Silva"? {"SILVA" in nome.upper()}')

