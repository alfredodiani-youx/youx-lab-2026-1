#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS
#for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

#idade da pessoa - tempo que trabalha + 35
from datetime import date
dados= dict()
dados['nome']= str(input("Digite seu nome :"))
nascimento=int(input("Digite sua data de nascimento :"))
dados['idade']= date.today().year - nascimento
carteiraTrabalho= int(input('Sua carteira de trabalho (digite 0 se nao tiver :'))
if carteiraTrabalho == 0:
    dados['ctps'] = 'Sem carteira.'
else:
    dados['ctps'] = carteiraTrabalho
    dados['anoContracao']= int(input("Digite o ano da sua contratação: "))
    dados['salario']= float(input("Digite qual é o seu salário: "))
    dados['aposentadoria'] = dados["anoContracao"] + 35
    idadeAposentado = dados['aposentadoria'] - nascimento
    print(f'Você iria se aposentar com {idadeAposentado} anos.')

print(dados)




