expressao = input("Digite a expressão: ")
lista = []
for caracteres in expressao:
    if caracteres == "(":
        lista.append(caracteres)
    elif caracteres == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break

if len(lista) == 0:
    print("Expressão válida!")
else:
    print("Expressão incorreta!")