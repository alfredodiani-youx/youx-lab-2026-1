
numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

chance = int(input('digite um numero entre 0 e 20: '))
while chance > 20 or chance < 0:
    print('numero INVALIDO!')
    chance = int(input('digite um numero entre 0 e 20: '))

print(numero[chance])
print('FIM')