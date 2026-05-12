#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Lapis" , 1.75, "Borracha" , 2.00, "Caderno" , 15.00, "Regua" , 3.50, "Transferidor" , 4.20, "Caneta" , 2.50, "Compasso" , 9.99, "Livro" , 34.00, "Mochila" , 120.65)
print('='*40)
print("Listagem de preços")
print('='*40)
for c in range(len(produtos)):
    print(f"{produtos[c]:.<40}")