from random import randint
print("Pensei em um número, consegue adivinhar-lo?")
t = 1;
s = int(input("Digite um número: "))
n = randint(0, 10)
while s != n:
    t += 1
    if s > n:
        s = int(input("Menor... Tente novamente: "))
    elif s < n:
        s = int(input("Maior... Tente novamente: "))
print("Meus parabéns! você acertou em {} tentativas".format(t))