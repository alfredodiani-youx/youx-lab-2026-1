expressao = input('digite a expressao: ')
lista = []

for caractere in expressao:
    if caractere == "(":
        lista.append(lista)
    elif caractere == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break

if len(lista) == 0:
    print('expressao VALIDA')

else:
    print('expressao INCORRETA')