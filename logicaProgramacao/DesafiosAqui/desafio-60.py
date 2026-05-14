numero=int(input('Digite um número: '))
if (numero == 1) or (numero == 0):
    print("O fatorial é 1")
else:
    valor = 1
    for c in range(1,numero+1):
        valor = valor * c
    print(valor)
