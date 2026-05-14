import random
numero=int(input('Adivinhe o número de 0 a 10 que eu estou pensando: '))
lista=[0,1,2,3,4,5,6,7,8,9,10]
n1=random.choice (lista)
while numero != n1:
    numero=int(input('Errou, tente denovo: '))
print('Acertou!')