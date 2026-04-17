num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} para binário é igual a: {}'.format(num , bin(num)))
elif opcao == 2:
    print('{} para octal é igual a: {}'.format(num , oct(num)))
elif opcao == 3:
    print('{} para hexadecimal é igual a: {}'.format(num , hex(num)))
else:
    print('Escolha uma opção entre 1, 2 e 3!')