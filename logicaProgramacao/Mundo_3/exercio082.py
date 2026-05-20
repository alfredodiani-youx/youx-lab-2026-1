#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

resp = 's'
num = list()
pares = list()
impares = list()
while resp == 's':
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N]'))
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista  completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A losta de impares é {impares}')