l = []
i = []
p = []
co = 0
while True:
    co += 1
    v = int(input(f"Digite o {co}° valor: "))
    o = input("Deseja adicionar mais valores? [S/N]: ").strip()[0]
    l.append(v)
    if v % 2 == 0:
        p.append(v)
    else:
        i.append(v)
    if o in "Nn":
        break
print(f"A lista completa é: {l}")
print(f"A lista de pares é: {p}")
print(f"A lista de ímpares é: {i}")