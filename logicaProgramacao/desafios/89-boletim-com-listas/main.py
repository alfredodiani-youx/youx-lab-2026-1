j = []
l = []
while True:
    j.append(input("Nome: "))
    j.append(float(input("Nota 1: ")))
    j.append(float(input("Nota 2: ")))
    l.append(j[:])
    j.clear()
    o = input("Deseja continuar? [S/N]: ").strip()[0]
    if o in "Nn":
        break
print("-"*30)
print(f'{"N°.":<4} {"NOME":<15} {"MÉDIA":>5}')
for i in l:
    media = (i[1] + i[2]) / 2
    print(f'{l.index(i):<4} {i[0]:<15} {media:>5.1f}')
print("-"*30)
while True:
    a = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if a == 999:
        break
    if a < len(l):
        print(f"Notas de {l[a][0]} são: {l[a][1]}, {l[a][2]}")
        print("-"*30)
    else:
        print("Aluno invalido! tente novamente.")