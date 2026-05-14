def verificarInteiro(numero):
    try:
        int(numero)
    except:
        return False
    else:
        return True
def verificarReal(numero):
    try:
        float(numero)
    except:
        return False
    else:
        return True
valor = input("Digite um número: ")
if verificarInteiro(valor):
    print("O número é inteiro")
else:
    while not verificarInteiro(valor):
        print("Erro: o valor não é inteiro!")
        valor = input("Digite um número: ")

if verificarInteiro(valor):
    if verificarReal(valor):
        print('')