#Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# cont = ('zero', 'um', 'dois', 'trem', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
#         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
# while True:
#     numero= int(input('Digite um numero: '))
#     if 0 <= numero <= 20:
#         print(f'voce pediu {cont[numero]}')
#         break
#     else:
#         print("Tente novamente.")

numerosExtenso = ('zero', 'um', 'dois', 'trem', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero= int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('tente novamente', end= ' ')
print(f'voce digitou o numero{numerosExtenso [numero]}')





