numeros = list()
numero = int(input('Digite um valor: '))
numeros.append(numero)
resposta = str(input('Quer continuar? [S/N] ')).upper()
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    numeros.append(numero)
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('-='*30)
print(f'Foram digitados {len(numeros)} valores')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')