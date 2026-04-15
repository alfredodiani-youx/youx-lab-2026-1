import random
print("-"*5, "Jogo de advinhar - tente advinhar o nome que eu estou pensando", "-"*5);
n = random.randint(0, 10);
n1 = int(input("Chute um número: "));
if n1 == n:
    print("Parabéns, você ganhou!!");
else: 
    print("Número incorreto, não foi dessa vez.")