n = int(input('Digite um numero: '))
contador = 0
atual = 0
ultimo = 0
while contador < n:
    if contador == 0:
        print('atal')
        contador += 1
    elif contador == 1:
        atual = 1
        print(atual)
        contador += 1
    else:
        resultado = atual + ultimo
        print(resultado)
        ultimo = atual
        atual = resultado
        contador += 1

