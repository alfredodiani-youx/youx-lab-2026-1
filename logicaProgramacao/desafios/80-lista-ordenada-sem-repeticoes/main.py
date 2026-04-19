l = []
co = 0
while True:
    co += 1
    v = int(input(f"Digite um valor: "))
    if v not in l:
        l.append(v)
        l.sort()
        lu = l.index(v)
        if co == 1:
            print("Valor adicionado a lista!")
        else:
            print(f"O número {v} foi adicionado na posição {lu} da lista")
    else:
        print(f"o número {v} já foi adicionado!")
        co -= 1
    if co == 5:
        break
print("-"*20)
print(f"Os valores em ordem foram: {l}")