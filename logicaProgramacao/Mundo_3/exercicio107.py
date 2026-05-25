#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
#e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import ex107.moeda.main
from logicaProgramacao.Mundo_3.ex107.moeda import main

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${main.metade(p)}')
print(f'O dobro de R${p} é de R${main.dobro(p)}')
print(f'Aumentando 10%, temos R${main.aumentar(p, 10)}')

