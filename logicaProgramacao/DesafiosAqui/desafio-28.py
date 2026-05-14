import random
numero=int(input('Adivinhe o número de 1 a 5 que eu estou pensando: '))
lista=[1,2,3,4,5]
n1=random.choice (lista)
if  numero == n1:
    print('Você acertou! :)')
else:
    print('Você errou :(')


