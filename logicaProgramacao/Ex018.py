import math

Numero = float(input('Digite o angulo em graus: '))
radian = math.radians(Numero)
seno = math.sin(radian)
cosen = math.cos(radian)
tangente = math.tan(radian)

print('O angulo de {} tem SENO de {:.2f}'.format(Numero, seno))
print('O angulo de {} tem o COSEN de {:.2f}'.format(Numero,cosen))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(Numero,tangente))