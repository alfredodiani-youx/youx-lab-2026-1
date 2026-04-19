from random import randint
l = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
ma = 0
me = 0
print(f"Os números sorteados foi: ", end="")
for n in range(len(l)):
    if n == 0:
        ma = l[0]
        me = l[0]
    if l[n] > ma:
        ma = l[n]
    elif l[n] < me:
        me = l[n]
    if n == len(l)-1:
        print(f"{l[n]} ", end="\n")
    else:
        print(f"{l[n]}, ", end="")
print(f"O maior número sorteado foi {ma} e o menor foi {me}")