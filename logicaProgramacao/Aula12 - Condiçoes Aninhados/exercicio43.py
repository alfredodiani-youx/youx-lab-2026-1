#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#    IMC abaixo de 18,5: Abaixo do Peso
#    Entre 18,5 e 25: Peso Ideal
#    25 até 30: Sobrepeso
#    30 até 40: Obesidade
#    Acima de 40: Obesidade Mórbida
altura = float(input("Digite sua altura(M): "))
if altura.is_integer():
    altura = altura / 100
peso = float(input("Digite seu peso(Kg): "))
imc = peso / ( altura * altura )
print(f"Seu imc é {imc:.1f}")
if imc < 18.5:
    print("Voce esta abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")

