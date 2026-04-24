r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if (r1 < r2 + r3) and (r1 < r3 + r2) and (r2 < r1 + r3):
    print('As 3 retas formam um triangulo')
else:
    print('As 3 retas não formam um triangulo')