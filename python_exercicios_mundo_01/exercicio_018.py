from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
print('O ângulo de {},tem o seno de {}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {}, tem o cosseno de {}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {}, tem o tangente de {}'.format(angulo, tangente))
