#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

    #IMC abaixo de 18,5: Abaixo do Peso
    #Entre 18,5 e 25: Peso Ideal
    #25 até 30: Sobrepeso
    #30 até 40: Obesidade
    #Acima de 40: Obesidade Mórbida


peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
indice_massa_corporal = peso / (altura ** 2)
if indice_massa_corporal < 18.5:
    print("Abaixo do peso")
elif indice_massa_corporal >= 18.5 and indice_massa_corporal < 25:
    print("Peso ideal")
elif indice_massa_corporal >= 25 and indice_massa_corporal < 30:
    print("Sobrepeso")
elif indice_massa_corporal >= 30 and indice_massa_corporal < 40:
    print("Obesidade")
elif indice_massa_corporal > 40:
    print("Obesidade Mórbida")
