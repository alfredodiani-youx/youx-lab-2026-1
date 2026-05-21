n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
n3 = float(input('Terceira Nota: '))
media = (n1 + n2 + n3) / 2
print('tirando a nota {:.1f} e {:.1f} é {:.1f}, a media do aluno é {:.1f}'.format(n1, n2, n3, media))
if media >=5 and media <7:
    print('\033[35mO Aluno esta de RECUPERAÇÃO')
elif media <=5:
    print('\033[31mO Aluno esta REPROVADO')
elif media >=7:
    print('\033[32mO Aluno esta APROVADO')