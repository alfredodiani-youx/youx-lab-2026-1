expressao = input("Digite a expressão: ")
lista = []
for listagem in expressao:
    if listagem == "(":
        lista.append(listagem)
    elif listagem == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break

if len(lista) == 0:
    print("Expressão válida!")
else:
    print("Expressão incorreta!")