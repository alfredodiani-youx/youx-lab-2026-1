lista = []
pares = [0,2,4,6,8]
listaP = []
impares = [1,3,5,7,9]
listaI = []
testPI = 0
N = 0
clean = []
N = int(input('Digite um valor: '))
lista.append(N)
testPI = int(str(N)[-1])
if testPI in pares:
    listaP.append(N)
elif testPI in impares:
    listaI.append(N)
SN = str(input('Quer continuar? [S/N] ').upper().strip())
while SN != 'N':
    N = int(input('Digite um valor: '))
    lista.append(N)
    testPI = int(str(N)[-1])
    if testPI in pares:
        listaP.append(N)
    elif testPI in impares:
        listaI.append(N)
    SN = str(input('Quer continuar? [S/N] ').upper().strip())
print(f'A lista completa é {lista}')
if listaP != clean:
    print(f'A lista de pares é {listaP}')
else:
    print('Não existe lista de pares.')
if listaI != clean:
    print(f'A lista de inpares é {listaI}')
else:
    print('Não existe lista de inpares.')
