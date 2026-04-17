nt1 = float(input('Quanto voce tirou na 1º prova?: '))
nt2 = float(input('Quanto voce tirou na 2º prova?: '))
media = ((nt1 + nt2)/2)

print('com as notas de {} e {}, sua média é de {}.'.format(nt1 , nt2 , media))
if media < 5:
    print('O aluno está reprovado!')
elif media >= 5 and media <= 7.9:
    print('O aluno está de recuperação.')
elif media >= 7 and media:
    print('O aluno está aprovado!')
