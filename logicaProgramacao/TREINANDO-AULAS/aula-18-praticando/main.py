galera = list()
dado = list()
for c in range(0, 2):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

    print(galera)