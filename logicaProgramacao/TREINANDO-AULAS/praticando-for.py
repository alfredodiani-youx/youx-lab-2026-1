lista = [['bia', 15]]
for pessoa in lista:
    nome = pessoa[0]
    idade = pessoa[1]
    print(pessoa)
    print(nome)
    print(idade)
    if idade > 5:
        print('nao é criança')