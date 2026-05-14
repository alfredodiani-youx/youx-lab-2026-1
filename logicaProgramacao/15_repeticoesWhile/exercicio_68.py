from random import randint
v= 0
while True:
    jogador= int(input("diga um valor :"))
    computador= randint(0 , 10)
    total= jogador + computador
    tipo= ' '
    while tipo not in 'PI':
        tipo= str(input("par ou impar?[P/I] :")).strip().upper()
    print(f'voce jogou {jogador} e o computador jogou {computador}, no total deu {total} ')
    if total % 2 == 0:
        print("deu par")
    else:
        print('deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print("voce venceu")
            v += 1
        else:
            print("voce perdeu")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("voce venceu")
            v += 1
        else:
            print("voce perdeu")
            break
    print("vamos jogar novamente")