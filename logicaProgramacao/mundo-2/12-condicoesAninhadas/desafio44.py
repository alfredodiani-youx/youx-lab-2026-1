v = float(input('Qual e o valor do produto? '))
p = int(input('Qual a forma de pagamento?' 
              ' 1: A vista'
              ' 2: Cartão'
              ' 3: 2 vezes no cartão'
              ' 4: 3 ou mais vezes no cartão '))
if p == 1:
    print(f'O valor sera de R${v - (10/100 * v):.2f}')
elif p == 2:
    print(f'O valor sera de R${v - (5/100 * v):.2f}')
elif p == 3:
    print(f'O valor sera de R${v:.2f}')
else:
    print(f'O valor sera de R${v + (20/100 * v):.2f}')