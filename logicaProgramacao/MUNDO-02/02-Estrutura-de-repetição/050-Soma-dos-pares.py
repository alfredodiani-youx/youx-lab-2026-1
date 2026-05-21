from future.standard_library import import_top_level_modules

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
from tqdm import tqdm
import time
for i in tqdm(range(108), colour='#B0C4DE', desc='analisando o numero {}'.format(soma)):
    time.sleep(0.1)
print('\033[34mvoce informou {} número PARES soma foi de {}'.format(cont, soma ))
