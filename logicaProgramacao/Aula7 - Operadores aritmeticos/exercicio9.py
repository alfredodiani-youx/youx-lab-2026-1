#Leia o numero digitado pelo usuario e mostre sua tabuada

n = int(input("Digite um numero para ser calculada a tabuada: "))
for t in range (1 , n +1):
 r = n * t
 print (f" {n} X {t} = {r} ")

