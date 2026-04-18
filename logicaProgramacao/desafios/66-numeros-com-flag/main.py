n = int(input("Digite um número (use 999 para sair): "))
t = 0
c = 0;
while True:
    if n != 999:
        c += 1
        t += n
        n = int(input("Digite um número (use 999 para sair): "))
    elif n == 999:
        break;
print("A soma dos {} valores deu {}".format(c, t))