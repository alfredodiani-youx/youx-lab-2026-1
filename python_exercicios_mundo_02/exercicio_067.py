#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.


while True :
    numero = int(input("Digite um número para ver sua tabuada: "))
    if numero < 0:
       break
    for contador in range (1,11):
        print(f"{numero} * {contador} = {numero * contador}")
print("Não é possivel fazer a tabuada com número negativo")
