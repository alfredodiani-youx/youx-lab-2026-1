v = int(input('Qual a velocida o carro passou no radar? '))
if v >80:
    print('A multa e de R${}' .format((v - 80)*7))
else:
    print('Não ultrapassou o limite de velocidade')