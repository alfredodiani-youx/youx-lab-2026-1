#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
from os.path import join

frase = input("Digite uma palavra ou frase para descobrir se a mesma é palindroma: ").upper().replace(' ', '')
separado = frase.split()
junto = ''.join(frase)
inverso = ''
for pa in range (len(junto) -1 , -1 , -1):
    inverso += junto[pa]
    print(inverso)
if inverso == junto:
    print(f"A palavra/frase digitada é palindroma")
else:
    print("Nao é palindroma")
