def inte(n):
    try:
        int(n)
    except:
        return False
    else:
        return True
def rea(n):
    try:
        float(n)
    except:
        return False
    else:
        return True
while True:
    n1 = input("Digite um número inteiro: ")
    if inte(n1):
        while True:
            n2 = input("Digite um número real: ")
            if rea(n2):
                print(f"O valor inteiro digitado foi {n1} e o valor real digitado foi {n2}")
                break
            else:
                print("ERRO: o valor digitado não é um número real")
        break
    else:
        print("ERRO: o valor digitado não é um número inteiro")