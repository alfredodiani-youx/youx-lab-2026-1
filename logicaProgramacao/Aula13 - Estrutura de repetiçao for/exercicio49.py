#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Digite um numero entre 1 e 10 para ver a sua tabuada: "))
for n in range ( 1 , 10 + 1):
 r = num * n
 print (f"{num} x {n} = {r}")