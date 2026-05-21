valor = float(input('qual e o valor da casa: R$' ))
salario = float(input('qual e o salario do comprador: '))
anos = int(input('quantos anos de finiciamento? '))
somas = valor/ (anos * 12)
minimo = salario * 30 / 100
print('pra pagar uma casa de R${} em {} anos'.format(valor, anos), end='')
print('a prestação sera de {:.2f}'.format(somas))
if salario < minimo:
    print('\033[32mIMPRESTIMO CONSEDIDO')
else:
    print('\033[31mIMPRESTIMO NEGADO')
