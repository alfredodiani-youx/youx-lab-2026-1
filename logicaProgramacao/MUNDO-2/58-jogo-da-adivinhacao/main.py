#o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
numeroAleatorio = randint(0,10) #variavel que registra numero aleatorio

chute = int(input('digite um numero entre 0 e 10: ')) #variavel que registra o chute

tentativas = 1 #registra o numero de tentativas

while numeroAleatorio != chute: #while = define que enquanto o chute for diferente de numeroAleatorio ficara em loop
    tentativas += 1
    print('voce esta incorreto,tente novamente')
    chute = int(input('digite um numero entre 0 e 10: '))  # variavel que registra o chute novamente
print(f'FIM,voce gastou {tentativas} tentativas')




