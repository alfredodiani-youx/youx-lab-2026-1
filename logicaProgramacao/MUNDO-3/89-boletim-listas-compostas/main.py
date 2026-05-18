aluno = []
lista = []
while True:
    aluno.append(input("Nome: "))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    lista.append(aluno[:])
    aluno.clear()
    opcao = input("Deseja continuar? [S/N]: ").strip()[0]
    if opcao in "Nn":
        break
print("-"*30)
print(f'{"N°.":<4} {"NOME":<15} {"MÉDIA":>5}')
for i in lista:
    media = (i[1] + i[2]) / 2
    print(f'{lista.index(i):<4} {i[0]:<15} {media:>5.1f}')
print("-"*30)
while True:
    a = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if a == 999:
        break
    if a < len(lista):
        print(f"Notas de {lista[a][0]} são: {lista[a][1]}, {lista[a][2]}")
        print("-"*30)
    else:
        print("Aluno invalido! tente novamente.")