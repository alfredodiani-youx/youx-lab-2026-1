from random import randint
lista = []
print("-"*25)
print("   JOGO DA MEGA SENA")
print("-"*25)
valor = int(input("Quantos jogos você quer que eu sorteie?: "))
print("--"*3, f"SORTEANDO {valor} JOGOS", "--"*3)
for i in range(0, valor):
    jogo = []
    while len(jogo) != 6:
        aleatorio = randint(1, 60)
        if aleatorio not in jogo:
            jogo.append(aleatorio)
        jogo.sort()
    lista.append(jogo[:])
    print(f"Jogo {i+1}: {jogo}")