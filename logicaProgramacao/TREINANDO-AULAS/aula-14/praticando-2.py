#Números Pares: Mostre todos os números pares entre 1 e 50.

contagem = 1
while contagem != 51:
    contagem += 1
    if contagem % 2 == 0:
        print(contagem)