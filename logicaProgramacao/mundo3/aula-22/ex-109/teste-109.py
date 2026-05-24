
import ex109 as moeda

preço = float(input('Digite seu preço: R$ '))

print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentado 10%, temos {moeda.aumentar(preço, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço, 13, True)}')