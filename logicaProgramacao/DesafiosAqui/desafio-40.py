nota1=float(input('Digite a nota da primeira prova: '))
nota2=float(input('Digite a segunda: '))
media=(nota1+nota2)/2
if media<5:
    print('REPROVADO')
elif media>6.9:
    print ('APROVADO')
else:
    print('RECUPERAÇÃO')

