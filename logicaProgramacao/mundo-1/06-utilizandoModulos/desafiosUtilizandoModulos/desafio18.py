import math
a = int(input('digite um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t =math.tan(math.radians(a))
print('O seno e {}, o cosseno e {} e a tangente e {}' .format(s, c, t))