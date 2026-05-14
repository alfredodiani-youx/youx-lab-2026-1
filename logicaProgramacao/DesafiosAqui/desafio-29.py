km=int(input ('A quantos km o carro anda? '))
n1=(km-80)*7.0
if km <= 80:
    print('parabéns por dirigir certo!')
else:
    print(f'você passou acima do limite a multa é de {n1} reais.')
