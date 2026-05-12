#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

num1 = int(input("Digite um numero inteiro: "))
print ("Escolha uma opçao: ")
print("[1] Binaria")
print("[2] Octal" )
print("[3] Hexagonal")
escolha = int(input(""))
if escolha  == 1:
 print(f"{num1} convertido para binario é {bin(num1)}")
elif escolha == 2:
 print(f"{num1} convertido para octal é {oct(num1)}")
elif escolha == 3:
 print(f"{num1} convertido para hexadecimal é {hex(num1)}")
else:
    print("Valor invalido")