ano=int(input('Digite um ano para saber se é bissexto: '))
cl=ano%4==0
if cl:
    print(f'{ano} é um número bissexto')
else:
    print(f'{ano} não é um ano bissexto')
