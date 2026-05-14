valor=float(input('Digite o valor da casa: '))
salario=float(input('Digite seu salário: '))
anos=float(input('Digite por quantos anos você vai pagar: '))
meses=anos*12

pagar=valor/meses

porcent= (pagar*30)/100

porcento=(salario*30)/100

if porcento>pagar:
    print (f'Você vai pagar {pagar:.2f} por mês.')
    print('O EMPRÉSTIMO PODE SER CONCEDIDO!')
else:
    print('Você não pode pegar o empréstimo')