dados = []
lista = []
ma = me = 0
while True:
    dados.append(input("nome: "))
    dados.append(int(input("peso: ")))
    if len(lista) == 0:
        ma = dados[1]
        me = dados[1]
    else:
        if dados[1] >= ma:
            ma = dados[1]
        if dados[1] <= me:
            me = dados[1]
    lista.append(dados[:])
    dados.clear()
    o = input("Deseja continuar? [S/N]: ").strip()[0]
    if o in "Nn":
        break
print(f"Ao todo você cadastrou {len(lista)} pessoas")
print(f"O maior peso registrado foi {ma}Kg. Peso de ", end="")
cf = 0
for i, e in enumerate(lista):
    cf += 1
    if e[1] == ma:
        if cf == len(e):
            print(f"{e[0]}")
        else:
            print(f"{e[0]}, ", end="")
if ma == me:
    print(f"O menor peso registrado também foi {ma}Kg!")
else:
    print(f"O menor peso registrado foi {me}Kg. Peso de ", end="")
    cf2 = 0
    for i, e in enumerate(lista):
        cf2 += 1
        if e[1] == me:
            if cf2 == len(e):
                print(f"{e[0]}")
            else:
                print(f"{e[0]}, ", end="")