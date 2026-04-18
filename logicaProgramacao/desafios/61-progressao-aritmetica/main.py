p = int(input("Digite o primeiro termo: "));
r = int(input("Digite a razão: "));
t = p
c = 1
while c <= 10:
    print("{} -> ".format(t), end="")
    t += r
    c += 1
print("Fim")