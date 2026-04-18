while True:
    v = int(input("Quer ver a tabuada de qual valor?: "))
    print("-"*20)
    if v > 0:
        for i in range(0, 10):
            print("{} x {} = {}".format(v, i+1, v*(i+1)))
        print("-"*20)
    else:
        print("PROGRAMA TABUADA ENCERRADA, VOLTE SEMPRE!")
        break