pr=float(input('Digite o primeiro valor: '))
sg=float(input('Digite o segundo: '))
ter=float(input('Digite o terceiro: '))
lista=  (pr+sg+ter)
if pr>sg and pr>ter:
    maior=pr
if sg>pr and sg>ter:
    maior=sg
if ter>pr and ter>sg:
    maior=ter
resultado = (lista - maior)
if resultado>maior:
    print('Pode fazer um triângulo')
else:
    print('Não pode fazer um triângulo')
