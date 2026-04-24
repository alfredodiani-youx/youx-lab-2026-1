n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite outra nota: '))
if (n1 + n2) / 2 < 5:
    print('Voce foi reprovado')
elif (n1 + n2) / 2 > 5 and (n1 + n2) / 2 < 6.9:
    print('Voce esta de recuperação')
else:
    print('Voce foi aprovado. Parabens!')