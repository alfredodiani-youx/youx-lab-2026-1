import bisect
numeres = []
for pergunta in range(0, 6):
    numero =int(input('me duga um numero: '))
    bisect.insort(numeres, numero)
    print(f'numero {numero} incluido na posicao {numeres.index(numero)}')
print(f'numros digiados: {numeres}')




