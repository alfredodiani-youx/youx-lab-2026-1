#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input("Digite uma frase qualquer: "))
juntarFrase = frase.replace(" ",'')
juntaFraseInvertida = juntarFrase[::-1]
print(f"Essa aqui é a minha frase invertida {juntaFraseInvertida}")
if juntarFrase == juntaFraseInvertida:
    print("É palíndromo.")
else:
    print("Não é palíndromo!")
