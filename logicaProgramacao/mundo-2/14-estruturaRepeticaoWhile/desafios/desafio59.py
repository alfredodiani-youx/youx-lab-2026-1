num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
o = 0
while o != 5:
    print('''    1: somar 
    2: multiplicar 
    3: maior 
    4: novos numeros 
    5: sair''')
    o = int(input('O que você quer fazer: '))
    if o == 1:
        print(f'A soma de {num1} com {num2} e iqual a {num1 + num2}')
    elif o == 2:
        print(f'O produto de {num1} e {num2} e igual a {num1 * num2}')
    elif o == 3:
        if num1 < num2:
            print(f'{num2} e maior que {num1}')
        else:
            print(f'{num1} e maior que {num2}')
    elif o == 4:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
print('Obrigado, volte sempre')