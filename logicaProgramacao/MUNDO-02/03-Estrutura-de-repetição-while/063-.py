print("Sequencia Fibonacci")
n = int(input("Quantos termos voce quer mostrar na sequencia? "))
c = 0
segundo = c
proximo = 1
print('0', end=" ")
while c <= n -2:
    print(proximo, end=' > ')
    c += 1
    proximo += segundo
    segundo = proximo-segundo
print("Fim")