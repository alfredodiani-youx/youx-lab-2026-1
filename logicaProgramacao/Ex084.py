maior = menor = 0
arquivo = list()
pesos  = list ()
while True:
    print('-=-' * 10)
    arquivo.append(str(input('Digite o nome do individuo: ')))
    arquivo.append(int(input('Digite o peso do individuo: ')))
    if len(pesos) == 0:
        maior = menor = arquivo[1]
    else:
        if arquivo[1] > maior:
            maior = arquivo[1]
        if arquivo[1] < menor:
            menor = arquivo[1]
    pesos.append(arquivo[:])
    arquivo.clear()
    continuacao = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if continuacao == 'N':
        break
print('-=-' * 10)

for p in pesos:
    if p[1] == maior:
        print(f"{p[0]}", end= ' ')

for p in pesos:
    if p[1] == menor:
        print(f"{p[0]}", end='')

print(f"Foram pesadas {len(pesos)} pessoas")

