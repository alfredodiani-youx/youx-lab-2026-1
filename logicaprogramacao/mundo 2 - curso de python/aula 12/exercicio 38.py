numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
if numero1 > numero2:
    print('O primeiro é maior.')
elif numero2 > numero1:
    print('O segundo é maior.')
elif numero1 == numero2:
    print('Os valores são iguais.')
else:
    print('Não existe valor maior.')
