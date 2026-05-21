#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


produtos = ("Lápis............................R$    1,75"   ,
            "Caderno..........................R$    15,90"  ,
            "Estojo...........................R$    25,00"  ,
            "Transferidor.....................R$    4,20"   ,
            "Compasso.........................R$    9,99"   ,
            "Mochila..........................R$    120,32" ,
            "Caneta...........................R$    22,30"  ,
            "Livro............................R$    34,90")
print("_" * 30)
print("       LISTAGEM DE PREÇOS     ")
print("_" * 30)
for i in range(0,len(produtos)):
    if i % 1 == 0:
        print(f"{produtos[i]}")
