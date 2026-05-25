from random import randint
jogos = []
lista = []
print("Jogos da MEGA SENA")
jogo = int(input("Quantos jogos voce quer que eu sorteie: "))
print(f"Sorteando {jogo} jogos")
for p in range(1 , jogo+1):
    for n in range (1, 6+1):
        resultado = randint(1, 60)
        if resultado not in lista:
            lista.append(resultado)
    jogos.append(lista[:])
    lista.clear()
for i, lista in enumerate(jogos):
    print(f"Jogo {i+1}: {lista}")
print("BOa sorte")