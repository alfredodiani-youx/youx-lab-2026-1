import datetime

ano = int(input('qual o seu ano de nascimento?: '))
anoAtual= datetime.datetime.now().year
idade = anoAtual - ano
if idade < 9:
    print("Categoria Mirim.")
elif idade < 14:
    print("Categoria Infantil.")
elif idade < 19:
    print("Categoria Junior.")
elif idade < 20:
    print("Categoria Sênior.")
else:
    print("Categoria Master.")
