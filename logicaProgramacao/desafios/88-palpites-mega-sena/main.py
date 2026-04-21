from random import randint
l = []
print("-"*25)
print("   JOGO DA MEGA SENA")
print("-"*25)
v = int(input("Quantos jogos você quer que eu sorteie?: "))
print("--"*3, f"SORTEANDO {v} JOGOS", "--"*3)
for i in range(0, v):
    j = []
    while len(j) != 6:
        r = randint(1, 60)
        if r not in j:
            j.append(r)
        j.sort()
    l.append(j[:])
    print(f"Jogo {i+1}: {j}")
print("-"*10, "< BOA SORTE >", "-"*10)