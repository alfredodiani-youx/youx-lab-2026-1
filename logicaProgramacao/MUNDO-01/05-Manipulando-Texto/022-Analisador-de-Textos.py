import tqdm

nome = str(input('Digite Seu Nome Completo: '))
from tqdm import tqdm
import time
for i in tqdm(range(40), colour="#00FF00", desc="Carregando"):
    time.sleep(0.1)
print('seu nome foi analizado com sucesso!')
print('seu nome em maiusculas e {}'.format(nome.upper()))
print('seu nome em minusculas e {}'.format(nome.lower()))
print('seu nome tem no total de {}'.format(len(nome)))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))