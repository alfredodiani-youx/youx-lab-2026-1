from random import randint
print("=-"*20+"\nVAMOS JOGAR PAR OU ÍMPAR\n" + "=-"*20)
pi = ""
w = int()
while True:
    r = randint(0, 10)
    print("-="*20)
    v = int(input("Diga um valor: "))
    pi = input("Par ou ímpar?: ").strip()[0]
    if (v + r) % 2 == 0:
        if pi in "Pp":
           print("Você jogou {} e eu {}, o resultado é PAR! você ganhou!!".format(v, r))
           w += 1
        elif pi in "Ii":
           print("Você jogou {} e eu {}, o resultado é PAR! você perdeu!!".format(v, r))
           print("Sequência de vitórias: {}".format(w))
           break
    elif (v + r) % 2 != 0:
        if pi in "Pp":
           print("Você jogou {} e eu {}, o resultado é ÍMPAR! você perdeu!!".format(v, r))
           print("Sequência de vitórias: {}".format(w))
           break
        elif pi in "Ii":
           print("Você jogou {} e eu {}, o resultado é ÍMPAR! você ganhou!!".format(v, r))
           w += 1