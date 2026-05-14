import math
n0 = int(input('digite um número de 0 a 9999: '))
u = n0 // 1 % 10
d = n0 // 10 % 10
c = n0 // 100 % 10
m =  n0 // 1000 % 10
print("""unidade: {}
dezena: {}
centena {}
milhar: {}""".format(u,d,c,m))
