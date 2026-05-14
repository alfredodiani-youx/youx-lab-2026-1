real = float(input('Quantos dinheiro você tem na carteira? '))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:2f}'.format(real, dolar))
