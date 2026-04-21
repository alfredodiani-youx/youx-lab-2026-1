p = []
i = []
lf = []
for c in range(0, 7):
    v = int(input(f"Digite o {c+1}° valor: "))
    if v % 2 == 0:
        p.append(v)
    elif v % 2 != 0:
        i.append(v)
lf.append(p)
lf.append(i)
print(f"Os valores pares foram: {lf[0]}")
print(f"Os valores ímpares foram: {lf[1]}")