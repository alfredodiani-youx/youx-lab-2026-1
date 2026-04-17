print('Olá, por favor, me informe:')
valorcasa = float(input('Qual o valor da casa desejada? R$'))
salario = float(input('Qual seu salário atual? R$'))
anos = int(input('Em quantos anos você pretende pagar a casa?'))
prestacao = (valorcasa / anos)

print('Para uma casa de R${}, em {} anos, a prestação será de {}'.format(valorcasa , anos , prestacao))

if prestacao > (30 * salario)/100:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprevado!')
