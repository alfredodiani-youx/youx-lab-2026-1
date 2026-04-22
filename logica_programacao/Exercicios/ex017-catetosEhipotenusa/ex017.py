
from math import sqrt

import math

C_oposto = float(input(' digite o comprimento do cateto oposto:'))
C_adjacente = float(input('digite o valor do cateto adjacente:'))
hipotenusa = math.sqrt(C_oposto + C_adjacente)
print(f'o comprimento da hipotenusa é:{hipotenusa}')