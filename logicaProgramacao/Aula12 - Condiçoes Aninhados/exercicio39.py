from datetime import date
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_atual = date.today().year
nascimento = int(input("Digite o ano em que voce nasceu: "))
idade = ano_atual - nascimento
if idade < 17:
    falta = idade - 18
    print(f"voce possui {idade} anos e falta {falta} anos para voce poder se alistar")
elif idade == 18:
    print(f"Voce possui {idade} e deve se alistar imediatamente")
else:
    passou = idade - 18
    print(f"Voce possui {idade} anos e deveria ter se alistado a {passou}")

