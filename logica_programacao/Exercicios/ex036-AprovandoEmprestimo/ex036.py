casa = float(input('qual o valor da casa? $'))
salario = float(input('qual o salario?'))
anosPagamento = int(input('quantos anos de financiamento? '))
tempo = casa/(anosPagamento) * 12
prestação = salario * 30/100
print(f'para pagar uma casa de {casa} em {anosPagamento}')
print(f'a prestação sera de {prestação}')
if tempo <= prestação:
 print('o emprestimo pode ser concedido!')
else:
 print('o emprestimo foi negado!')