#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
from random import randint
print("VAMOS JOGAR PAR OU IMPAR!!")
while True:
    c = random.randint(1,100)
    p = int(input("Diga um valor: "))
    pi = input("Par ou impar? [P/I]").upper()

    