#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import choice
print("Sou seu computador...\n Voce consegue adivinha em que numero entre 0 a 10 eu estou pensando?")
num = int(input("Digite seu palpite: "))
c = 0,1,2,3,4,5,6,7,8,9,10
resp = choice(c)
while num != resp:
    num = int(input("O seu palpite esta errado, tente novamente: "))
    if num > 10:
        print("O seu palpite deve ser entre os numeros 0 e 10")
    else:
       if num > resp:

            print("Voce esta perto, digite um numero menor")
       else:
            print("Voce esta perto, digite um numero maior")
print("Parabens voce acertou")
