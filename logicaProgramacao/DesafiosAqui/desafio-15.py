n0 = int(input('Por quanto dias foi alugado? '))
n1 = float(input ('quantos km foi rodado? '))
n2 = n0 * 60
n3 = n1 * 0.15
n4 = n3 + n2
print ('o total a pagar é R$:{:.2f}'.format (n4))