from multiprocessing import context

temporaria = []   #lista temporaria/guardar os valores temporariamente
principal = []    #lista principal
maior = menor = 0
contagem = 0

while True:
    temporaria.append(str(input('nome:  ')))
    peso = float(input('peso: '))
    temporaria.append(peso)
    principal.append(temporaria[:])
    temporaria.clear()
    opcao = input('quer continuar [S/N]')

    if contagem == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    contagem += 1
    if opcao in 'Nn':
        break

print("=>"*30)
print(f'os dados foram {principal}')
print(f'ao todo voce cadastrou {len(principal)} pessoas')
print(f'o maior peso cadastrado foi {maior}kg')
print(f'o menor peso cadastrado foi {menor}kg')