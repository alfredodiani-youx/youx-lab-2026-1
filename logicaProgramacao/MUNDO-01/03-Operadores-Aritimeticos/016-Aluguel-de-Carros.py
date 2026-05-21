dias = int(input('quantos dias alugado? '))
km = float(input('quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar e de R${}'.format(pago))