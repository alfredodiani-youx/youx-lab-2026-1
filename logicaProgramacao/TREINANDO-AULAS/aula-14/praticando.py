#Limite do Usuário: Peça ao usuário um número inteiro \(N\). Use o while para mostrar na tela todos os números de 0 até \(N\).

numero = int(input('digite um numero INTEIRO: '))
contagem = 0

while contagem != numero + 1:
    print(contagem)
    contagem += 1