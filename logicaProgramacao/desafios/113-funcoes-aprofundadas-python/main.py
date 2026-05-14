def leiaInt(inteiro):
    try:
        int(inteiro)
    except:
        return False
    else:
        return True

def leiaFloat(real):
    try:
        float(real)
    except:
        return False
    else:
        return True

inteiro = input('Digite um inteiro: ')
while not leiaInt(inteiro):
    print("ERRO: por favor, digite um número inteiro válido.")
    inteiro = input('Digite um inteiro: ')
real = input('Digite um real: ')
while not leiaFloat(real):
    print("ERRO: por favor, digite um número inteiro válido.")
    real = input('Digite um real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')