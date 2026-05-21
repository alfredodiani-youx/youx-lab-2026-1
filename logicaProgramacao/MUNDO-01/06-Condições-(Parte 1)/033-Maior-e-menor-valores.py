a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# MENOR NUMERO DIGITADO:
menor = a
if b >= a or b >= c:
    pass
else:
    menor= b
if c<a and c<b:
    menor = c
# MAIOR NUMERO DIGIADO:
meior = a
if b>a and b>c:
    maior= b
if c>a and c>b:
    maior = c
print('o menor valor digitado foi {} '.format(menor))
print('o maior valor digitado foi {} '.format(maior))
