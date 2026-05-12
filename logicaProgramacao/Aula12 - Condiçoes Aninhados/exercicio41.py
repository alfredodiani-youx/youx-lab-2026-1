#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#   Até 14 anos: INFANTIL
#   Até 19 anos: JÚNIOR
#   Até 25 anos: SÊNIOR
#   Acima de 25 anos: MASTER
from datetime import date
nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(f"O atleta tem {idade} anos")
if idade < 9:
    print("CLASSIFICAÇAO: MIRIM")
elif idade > 9 and idade <14:
    print(f"CLASSIFICAÇAO: INFANTIL")
elif idade > 14 and idade < 19:
    print("CLASSIFICAÇAO: JUNIOR")
elif idade > 19 and idade < 25:
    print("CLASSIFICAÇAO: SENIOR ")
else:
    print("CLASSIFICAÇAO: MASTER")