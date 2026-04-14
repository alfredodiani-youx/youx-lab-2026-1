d = int(input('Quantos dias foi alugado? '));
km = float(input('Quantos Km rodados? '));
valor = (d * 60) + (km * 0.15);
print('O valor total a pagar é de R${:.2f}'.format(valor));