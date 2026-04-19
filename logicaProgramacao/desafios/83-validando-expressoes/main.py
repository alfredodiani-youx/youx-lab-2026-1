e = input("Digite a expressão: ")
li = []
for l in e:
    if l == "(":
        li.append(l)
    elif l == ")":
        if len(li) > 0:
            li.pop()
        else:
            li.append(")")
            break

if len(li) == 0:
    print("Expressão válida!")
else:
    print("Expressão incorreta!")