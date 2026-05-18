from random import randint

numeros = (randint(0, 10 ),randint(0, 10),randint(0, 10),randint(0,10), randint(0, 10))

print(f'os valores sorteados foram {numeros}')
print(f'o MENOR numero foi {min(numeros)}')
print(f'o MAIOR numero foi {max(numeros)}')