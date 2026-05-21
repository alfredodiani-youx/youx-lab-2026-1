n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
opcao = ''

while opcao != 5:
    print(" [1] somar \n [2] multiplicar \n [3] maior\n [4] novos numero \n [5] sair do programa \n ")
    opcao = int(input("Qual a sua escolha? "))
    if opcao == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
    if opcao == 2:
        multiplicacao  = n1 * n2
        print(f"{n1} X {n2} = {multiplicacao}")
    if opcao == 3:
        if n1 > n2:
            print(f"O maior numero é {n1} e o menor numero é {n2}")
        else:
            print(f"O maior numero é {n2} e o menor numero é {n1}")
    if opcao == 4:
        n1 = int(input("Digite o novo valor: "))
        n2 = int(input("Digite o novo valor; "))
print("Programa encerrado")