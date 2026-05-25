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