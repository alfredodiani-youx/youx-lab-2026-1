from random import shuffle
numero1 = str(input('Primeiro aluno: '))
numero2 = str(input('Segundo aluno: '))
numero3 = str(input('Terceiro aluno: '))
numero4 =  str(input('Quarto aluno: '))
lista = [numero1, numero2, numero3, numero4]
print(lista)
shuffle(lista)
print(f'A ordem de apresentação será: {lista} ')
