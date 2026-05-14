from os.path import split

frase=str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
if inverso==junto:
    print(f'A palavra {junto} é um políndromo!')
else:
    print(f'A palavra {junto} não é uma palavra políndromo!')