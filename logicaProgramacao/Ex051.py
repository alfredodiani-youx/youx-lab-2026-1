Primeiro = int(input('Primeiro termo: '))
Razao = int(input('Digite qual a razao: '))
Decimo = Primeiro + (10 - 1) * Razao
for c in range(Primeiro, Decimo , Razao):
    print(c)