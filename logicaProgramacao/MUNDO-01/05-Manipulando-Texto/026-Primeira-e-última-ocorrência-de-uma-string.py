frase = str(input('Digite uma Frase: ')).upper()
print('a letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('a primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))
