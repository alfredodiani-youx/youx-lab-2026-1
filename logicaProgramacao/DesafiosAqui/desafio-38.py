pn=float(input('Digite um número: '))
sn=float(input('Digite outro: '))
if pn>sn:
    maior=pn
    print('O primeiro valor é maior')
elif pn<sn:
    maior=sn
    print('O segundo valor é maior')
else:
    print('Os dois tem o mesmo valor.')