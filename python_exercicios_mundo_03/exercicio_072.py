#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


contador = "zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"
numero = int(input("Digite um número entre 0 e 20: "))
while  numero <= 0 or numero >= 20:
    if numero < 0 or numero > 20:
        print("Número inválido")
        contador += 1
print(f"Voce digitou o numero {numero}")
