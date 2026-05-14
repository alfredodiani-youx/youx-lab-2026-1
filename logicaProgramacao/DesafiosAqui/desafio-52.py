numero=int(input('Digite um numero: '))
contador=0
for i in range (numero,0,-1):
    if numero%i==0:
        contador += 1
        #print(contador)
if contador == 2:
    print("É um número Primo!")
else:
    print("Não é um número Primo!")