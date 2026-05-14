n=int(input('Qual o seu salário? '))
n1=(n*15)/100+n
n2=(n*10)/100+n
if n <= 1250:
    print(f'Com aumento o salário fica {n1} reais.')
else:
    print(f'Com o aumento o salário fica {n2} reais.')
