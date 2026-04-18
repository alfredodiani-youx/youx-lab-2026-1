n = int(input("Digite um número: "))
f = 1;
c = n

# modo que fiz com for: (desconsiderar)
#print("Fatorial de {} é: ".format(n), end="")
#for i in range(0, n):
#    f *= n-i
#    if i+1 < n:
#        print("{}".format(n - i), end=" x ")
#    else:
#        print("{}".format(n - i), end=" = {}".format(f))


while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))