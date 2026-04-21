#O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluna: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentaçao sera ')
print(lista)
