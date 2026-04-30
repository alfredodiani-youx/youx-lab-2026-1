casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa /  (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de {casa}R$ em {anos} anos, a parcela sera de {parcela}')
if parcela <= minimo:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')



