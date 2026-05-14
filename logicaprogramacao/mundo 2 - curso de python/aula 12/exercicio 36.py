valor_da_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
quantidade_de_anos_pagamento = int(input('Em quantos anos você vai pagar a casa? '))
quantidade_prestacoes = quantidade_de_anos_pagamento * 12
valor_prestacao = valor_da_casa / quantidade_prestacoes

if valor_prestacao < ( salario * 0.3):
    print(f"Empréstimo aceito! Você irá pagar {quantidade_prestacoes} parcelas de R${(valor_prestacao)}")
else:
    print('Enmpréstimo negado!')
