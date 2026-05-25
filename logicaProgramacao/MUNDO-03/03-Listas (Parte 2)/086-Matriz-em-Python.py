matriz = [[0,0,0], [0,0,0],[0,0,0]]

for indice in range(0,3):
    linha = []
    for j in range(0,3):
        num = int(input(f"Digite um valor {indice} x {j}: "))
        linha.append(num)
        matriz[indice] = linha
for Indice in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[Indice][c]}]")
        print()