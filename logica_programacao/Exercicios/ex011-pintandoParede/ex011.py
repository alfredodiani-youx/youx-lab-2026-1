'''
Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
rendimento =float(input('qual o rendimento da tinta m2/l:'))
largura = float(input('digite o valor da largura:'))
altura = float(input('digite o valor da altura:'))
area = largura * altura
quantidadetinta= (area / rendimento)
print(f'a quantidade de tinta é{quantidadetinta}')