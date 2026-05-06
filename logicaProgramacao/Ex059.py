Primeiro = float(input('Digite o primeiro numero: '))
Segundo = float(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] Sair')
    opcao = int(input('Qual a opcao: '))
    if opcao == 1:
        soma = Primeiro + Segundo
        print(f"A soma entre {Primeiro} e {Segundo} e o valor {soma}")
    elif opcao == 2:
        multiplicar = Primeiro * Segundo
        print(f"A multiplicacao entre {Primeiro} e {Segundo} e o valor {multiplicar}")
    if opcao == 3:
        if Primeiro > Segundo:
            maior = Primeiro
            print(f"O maior entre {Primeiro} e {Segundo} e o valor {maior}")
        elif Primeiro < Segundo:
            maior = Segundo
            print(f"O maior entre {Primeiro} e {Segundo} e o valor {maior}")
    if opcao == 4:
        print('Informe os numeros novamente')
        Primeiro = float(input('Digite o primeiro numero: '))
        Segundo = float(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
print('Fim do programa')






