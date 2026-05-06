contador = 0
num = int(input('Digite um numero: '))

for c in range (num, 0, -1):
    if num % c == 0:
        contador += 1

if contador == 2:
    print("É um número primo!")
else:
    print("Não é um número primo")
