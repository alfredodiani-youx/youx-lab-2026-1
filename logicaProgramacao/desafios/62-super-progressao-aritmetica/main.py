p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
termo = p
t = 0
q = 10

while q != 0:
    contador = 1
    while contador <= q:
        print(f"{termo} -> ", end="")
        termo += r
        contador += 1
        t += 1
    print("PAUSA")
    q = int(input("Quantos termos você quer mostrar a mais? "))

print("Progressão finalizada com {} termos mostrados".format(t))