
def LeiaTnt (mensagem):
    ok = False
    valor = 0
    while True:
        número = str(input(mensagem))
        if número.isnumeric():
            valor = int(mensagem)
            ok = True
        else:
            print('\033[0;31mERRO! Tente novamente!\033[m')
        if ok:
            break
    return valor
número = int(input('Digite um ńumero: '))
print(f'Você acabou de digitar o número {número}')
