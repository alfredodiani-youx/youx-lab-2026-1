num = int(input('digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:'
[ 1 ] converter para BINARIO

[ 2 ] converter para OCTAL

[ 3 ] converter para HEXADECIMAL''')
opcao  = int(input('Sua opção: '))
if opcao == 1:
    print('\033[33m*-*-*' * 20)
    print('                            {} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
    print('*-*-*' * 20)
elif opcao == 2:
    print('\033[33m*-*-*' * 20)
    print('                            {} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
    print('\033[33m*-*-*' * 20)
elif opcao == 3:
    print('\033[33m*-*-*' * 20)
    print('                            {} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
    print('*-*-*' * 20)
else:
    print('\033[31m--=--' * 20)
    print('\033[31m                               Opção Invalida, Tente Novamente')
    print('--=--' * 20)