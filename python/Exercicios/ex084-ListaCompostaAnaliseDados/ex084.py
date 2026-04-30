perfil = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(perfil) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    perfil.append(dado[:])
    dado.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'Ao todo, foram feitos {len(perfil)} cadastros')
for pessoas in perfil:
    if pessoas[1] == maior:
        print(f'O maior peso foi de {pessoas[0]}, com {maior}Kg')
    if pessoas[1] == menor:
        print(f'O menor peso foi dde {pessoas[0]}, com {menor}Kg')
