lanche = ['picole', 'bolo', 'pudim', 'torta']
lanche[3] = 'frutas'

#para adicionar algo:
lanche.append('cookie')

#adicionar um elemento no meio de outros:
lanche.insert(2,'pao')

#PARA ELIMINAR UM ELEMENTO:
del lanche[3]
lanche.pop(3)
lanche.remove('pao')

#PARA REMOVER UM ELEMENTO QUE NAO EXISTE;
if 'pizza' in lanche:
    lanche.remove('pizza')

#listas em range:
valores = list(range(4, 11))
valores = [8, 2, 5, 7, 3]
valores.sort()
valores.sort(reverse=True)
len(valores)

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
valores.append(int(input('Digite um numero: ')))
