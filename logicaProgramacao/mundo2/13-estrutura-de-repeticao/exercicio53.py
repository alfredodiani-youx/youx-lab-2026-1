#Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.
palavra = str(input("digite uma palavra:")).replace(' ', '')
separando = palavra.strip()
junto = ''.join(separando)
inverso = ''
for i in range(len(junto)-1, -1, -1):
    inverso += junto
if inverso == junto:
    print( 'É PALINDROMO')
else:
     print('NÃO É PALINDROMO')
print(junto)

