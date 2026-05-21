from tqdm import tqdm
num = int(input('informe um numero: '))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
mi = num // 1000 % 10
m1 = num // 10000 % 10
ml = num // 100000 % 10
m = num // 1000000 % 10
from tqdm import tqdm
import time
for i in tqdm(range(15), colour='#00FFFF', desc='analisando o numero {}'.format(num)):
    time.sleep(0.1)
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena:{}'.format(c))
print('milhar:{}'.format(mi))
print('Dezena de Milhar:{}'.format(m1))
print('Centena de Milhar:{}'.format(ml))
print('Unidade de Milhão:{}'.format(m))
