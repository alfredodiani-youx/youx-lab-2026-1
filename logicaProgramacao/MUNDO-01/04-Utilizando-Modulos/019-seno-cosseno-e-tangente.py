#Exercício Python #018 - Seno, Cosseno e Tangente
from math import radians, sin,cos,tan
angolo = float(input("digite um angolo que deseja: "))
seno = sin(radians(angolo))
print('o angolo de {} tem o SENO de {:.2f}'.format(angolo, seno))
cosseno = cos(radians(angolo))
print('o angolo de {} tem o COSSENO de {:.2f}'.format(angolo, cosseno))
tangente = tan(radians(angolo))
print('o angolo de {} tem o TANGENTE de {:.2f}'.format(angolo, tangente))

