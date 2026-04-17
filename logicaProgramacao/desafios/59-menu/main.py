n1 = float(input("Digite um valor: "));
n2 = float(input("Digite outro valor: "));
o = str()
while o != 5:
    print("-"*5);
    print("1 - somar\n2 - multiplicar\n3 - maior\n4 - novos números\n5 - sair")
    o = int(input("Digite a opção: "));
    if o == 1:
        print("Aqui está o resultado da soma: {} + {} = {}".format(n1, n2, n1 + n2));
    elif o == 2:
        print("Aqui está o resultado da multiplicação: {} x {} = {}".format(n1, n2, n1 * n2));
    elif o == 3:
        if n1 > n2:
            print("O número {} é maior que o número {}".format(n1, n2))
        else:
            print("O número {} é maior que o número {}".format(n2, n1))
    elif o == 4:
        n1 = float(input("Digite um novo valor: "))
        n2 = float(input("Digite um segundo novo valor: "))