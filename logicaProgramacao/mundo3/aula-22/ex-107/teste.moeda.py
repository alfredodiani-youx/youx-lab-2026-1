from moeda import metade, dobro, aumentar

preço = (float(input('Digite seu preço: R$ ')))
print(f'A medate de {preço} é {metade(preço)}')
print(f'O dobro de {preço} é {dobro(preço)}')
print(f'Aumentado 10%, temos {aumentar(preço, 10)}')