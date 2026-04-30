numero = int(input('Digite um numero inteiro: '))
print ('''Escolha uma das bases para conversao: [1] converter para binario [2] converter para octal [3] converter para hexadecimal''')
opcao = int(input('Digite sua opcao: '))
if opcao == 1:
    print (f'{numero} convertido para binario e igual a {bin(numero)}')
elif opcao == 2:
    print(f'{numero} convertido para octal e igual a {oct(numero)}')
elif opcao == 3:
    print(f'{numero} convertido para hexadecimal e igual a {hex(numero)}')
else:
    print('Opcao invalida!')