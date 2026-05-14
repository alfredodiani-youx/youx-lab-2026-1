# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

primeira = float(input("Qual é o comprimento da primeira reta? "))
segunda = float(input("Qual é o comprimento da segunda reta? "))
soma = primeira + segunda
terceiro = float(input("Qual é o comprimento da terceira reta? "))
if soma > terceiro:
    print("Pode formar um triangulo")
else:
    print("nao pode formar triangulo")
