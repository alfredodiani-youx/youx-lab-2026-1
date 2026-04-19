co = 0
l = []
while True:
    co += 1
    n = int(input(f"Digite o {co}° número: "))
    if n not in l:
        l.append(n)
    else:
        print(f"O número {n} já foi registrado!")
        co -= 1
    o = input("Deseja continuar? [S/N]: ").strip()[0]
    if o in "Nn":
        l.sort()
        break
print(f"Você digitou os valores: {l}")