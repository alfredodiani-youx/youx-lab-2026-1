dados = []
lista = []
maior = menor = 0
opcao = 'S'
while opcao not in 'Nn':
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    pessoa = [nome, peso]
    if len(lista) == 0:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso <= menor:
            menor = peso
    lista.append(pessoa)
    opcao = input("Deseja continuar? [S/N]: ").strip()[0]
print(f"Ao todo você cadastrou {len(lista)} pessoas")
print(f"O maior peso registrado foi {maior}Kg. Peso de ", end="")
cf = 0
for i, e in enumerate(lista):
    cf += 1
    if e[1] == maior:
        if cf == len(e):
            print(f"{e[0]}")
        else:
            print(f"{e[0]}, ", end="")
if maior == menor:
    print(f"O menor peso registrado também foi {maior}Kg!")
else:
    print(f"O menor peso registrado foi {menor}Kg. Peso de ", end="")
    cf2 = 0
    for i, e in enumerate(lista):
        cf2 += 1
        if e[1] == menor:
            if cf2 == len(e):
                print(f"{e[0]}")
            else:
                print(f"{e[0]}, ", end="")