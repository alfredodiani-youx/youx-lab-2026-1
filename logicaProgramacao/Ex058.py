from random import randint
rand = randint(0, 10)
print('O Computador vai pensar em um numero entre 0 e 10')
cont = 0
Tentativa = int(input('Tente adivinhar o numero entre 0 e 10: '))
while Tentativa != rand:
    if Tentativa > rand:
        Tentativa = int(input('Voce errou,o numero e menor do que o que voce escolheu,tente novamente: '))
    elif Tentativa < rand:
        Tentativa = int(input('Voce errou,o numero e maior do que o que voce escolheu,tente novamente: '))
    cont += 1
cont += 1
print(f"VOCE ACERTOU O NUMERO {rand},E FOI PRECISO DE {cont} TENTATIVA(S)")