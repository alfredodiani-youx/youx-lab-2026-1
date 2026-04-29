from datetime import date
Ano = int(input('Ano de nascimento: '))
Idade = date.today().year - Ano
print(Idade)
print(f'O Atleta tem {Idade} anos')

if Idade < 9:
    print('Classificacao: MIRIM')
elif Idade < 14:
    print('Classificacao: INFANTIL')
elif Idade < 19:
    print('Classificacao: JUNIOR')
elif Idade < 25:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')