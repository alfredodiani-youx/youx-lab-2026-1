ma = 0
me = 0
s = "N"
m = 0;
co = 0
while s in "Nn":
    n = float(input("Digite o {}° valor: ".format(co+1)))
    if co == 0:
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        elif n < me:
            me = n
    co += 1
    m += n
    s = input("Deseja sair? [S/N]: ").strip()
print("Você digitou {} números, e a média foi {}".format(co, m / co))
print("o maior número foi {} e o menor foi {}".format(ma, me))