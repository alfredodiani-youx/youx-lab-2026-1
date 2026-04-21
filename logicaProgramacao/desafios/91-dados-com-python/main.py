from operator import itemgetter
from time import sleep
from random import randint
j = {
    "jogador 1": randint(1, 6),
    "jogador 2": randint(1, 6),
    "jogador 3": randint(1, 6),
    "jogador 4": randint(1, 6)
}
l = [j]
for i, e in j.items():
    sleep(0.5)
    print(f"o {i} tirou {e} no dado!")
print("--"*20)
s = "    "
print(f"{s}== RANKING DOS JOGADORES ==")
ra = sorted(j.items(), key=itemgetter(1), reverse=True)
co = 1
for i, k in ra:
    sleep(0.5)
    print(f"{s}{co}° lugar: {i}, tirou {k} no dado")
    co += 1