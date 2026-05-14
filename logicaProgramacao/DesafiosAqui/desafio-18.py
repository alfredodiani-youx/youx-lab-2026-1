import math
n0 = float(input('digite qualquer ângulo: '))
seno = math.sin(math.radians(n0))
print  ('O ângulo de {} tem o SENO de {:.2f}.'.format(n0, seno))
cosseno = math.cos(math.radians(n0))
print ('O ângulo de {} tem o COSSENO de {:.2f}'.format(n0, cosseno))
tangente = math.tan(math.radians(n0))
print ('O ângulo de {} tem o TANGENTE de {:.2f}'.format(n0, tangente))