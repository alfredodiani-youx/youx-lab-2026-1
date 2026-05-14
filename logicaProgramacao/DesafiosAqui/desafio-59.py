numero=int(input('Digite um valor: '))
outroNumero=int(input('Digite outro: '))
escolhido= None
while escolhido !=5:
    print("""[1] somar.
[2] multiplicar.
[3] maior.
[4] novos números.
[5] sair do programa.""")
    escolhido = int(input('R: '))
    valor=None
    if escolhido ==1:
        valor=numero+outroNumero
        print(valor)
        print('Fim')
    elif escolhido ==2:
        valor=numero*outroNumero
        print(valor)
        print('Fim')
    elif escolhido ==3:
        if numero>outroNumero:
            print(f'O maior número é {numero}')
            print('Fim')
        else:
            print(f'O maior número é {outroNumero}')
    elif escolhido ==4:
        numero = int(input('Novo valor: '))
        outroNumero = int(input('Outro novo  valor: '))

print('Você saiu.')