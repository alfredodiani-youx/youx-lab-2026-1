#Crie um codigo que receba um valor e calcule quanto esse valor ficaria com 5% de desconto

produto = float(input("Digite o preço do produto: R$"))
desconto = produto - ( produto * 5  / 100 )
print(f"O valor do produto é R${produto:.2f} e com 5% de desconto fica R${desconto:.2f}")