notaum =float(input('PRIMEIRA NOTA: '))
notadois =float(input('SEGUNDA NOTA:'))
media = (notaum+notadois) /2
print(media)
if media < 5:
    print(f'Sua média é {media}: REPROVADO!')
elif media > 5 and media < 6.9:
    print(f'Sua média é {media}: RECUPERAÇÃO!')
elif media > 7:
    print(f'Sua média é {media}: APROVADO!')

