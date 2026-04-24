num1 = int(input('Digite um numero: '))
num2 = int(input('Outro numero: '))
if num1 < num2:
    print(f'{num1} e menor que {num2}')
elif num1 > num2:
    print(f'{num2} e menor que {num1}')
else:
    print('Os numeros são iguais')