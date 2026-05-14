import random
print("""Vamos jogar jokenpô, escolha um dos três. 
pedra[1] 
papel [2]
tesoura[3]""")
escolha=int(input('R: '))
lista=[1,2,3]
print(escolha)
bot=random.choice(lista)
print(bot)

if bot == 2 and escolha == 1:
    print('GANHEI!;>')
if bot == 3 and escolha == 1:
    print('PERDI!;<')
if bot == 1 and escolha == 1:
    print('EMPATE!')
if bot == 2 and escolha == 2:
    print('EMPATE')
if bot == 3 and escolha == 2:
    print('GANHEI!')
if bot == 1 and escolha == 2:
    print('PERDI!')
if bot == 3 and  escolha == 3:
    print('EMPATE')
if bot == 2 and escolha == 3:
    print('PERDI!')
if bot == 1 and escolha == 3:
    print('GANHEI!')