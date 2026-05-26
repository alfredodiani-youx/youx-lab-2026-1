cont =('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero =int(input('digite um numero entre 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('tente novamente. ', end='')
print(f'voce digitou o numero {cont[numero]}')