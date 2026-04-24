import random
lista = (['pedra' , 'papel' , 'tesoura'])
pc = random.choice(lista)
e = str(input('pedra, papel ou tesoura? '))
if pc == 'pedra' and e == 'papel':
    print('Parabens! Você ganhou, escolhi pedra')
elif pc == 'papel' and e == 'tesoura':
    print('Parabens! Você ganhou, escolhi papel')
elif pc == 'tesoura' and e == 'pedra':
    print('Parabens! Você ganhou, escolhi tesoura')
elif pc == 'papel' and e == 'pedra':
    print('Você perdeu, escolhi papel')
elif pc == 'pedra' and e == 'tesoura':
    print('Você perdeu, escolhi pedra')
elif pc == 'tesoura' and e == 'papel':
    print('Você perdeu, escolhi tesoura')
else:
    print('Empate')