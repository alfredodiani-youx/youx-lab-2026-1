
#Exercício Python 076: Crie um programa que tenha uma tupla única
#com nomes de produtos e seus respectivos preços,na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular

listagem = ('rimel',  15.50,
            'gloss', 10.65,
            'batom', 18.20,
            'pincel', 5,99,
            'base', 25.90,
            'primer', 12.60,
            'esponjinha', 10.90,
            'fixador', 22.30,
            'contorno', 15.90,
            'iluminador', 12.99)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for pos  in range (0, len(listagem)):
    if pos % 2  == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:<10}')