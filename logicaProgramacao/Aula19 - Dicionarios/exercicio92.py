#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
dados = {}
dados['NOME'] = input("Informe o seu nome: ").strip().capitalize()
nascimento = int(input("Digite o ano do seu nascimento: "))
dados['IDADE'] = date.today().year - nascimento
dados['CTPS'] = int(input("Numero da CTPS [DIGITE 0 SE NAO TIVER]: "))
if dados['CTPS'] != 0:
    dados['ADC'] = int(input("Digite o ano de contrataçao: "))
    dados['SALARIO'] = float(input("Salario: R$"))
    dados['APOSENTADORIA'] = (dados['ADC'] + 35) - nascimento
    for k, v in dados.items():
        print(f"{k}: {v}")

