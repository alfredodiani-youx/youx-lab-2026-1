nota1 = float(input('primeira nota:'))
nota2 = float(input('segunda nota:'))
media= (nota1 + nota2) / 2
if media < 5.0:
    print('voce foi reprovado')
elif media == 5.0 or 6.9:
    print('voce esta de recuperação')
elif media >= 7.0:
    print('voce foi aprovado')