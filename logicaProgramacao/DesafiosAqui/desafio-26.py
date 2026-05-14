from itertools import count

a=str(input('digite algo: ')).upper().strip()
print('A letra aparece {} vezes na frase.'.format(a.count('A')))
print('A posição do primeiro A é: {} '.format(a.find('A')+1))
print('A última posição do A é: {} '.format(a.rfind('A')+1))