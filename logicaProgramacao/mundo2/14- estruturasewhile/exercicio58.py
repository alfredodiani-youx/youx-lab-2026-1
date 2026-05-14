# Exercício Python 058: Melhore o jogo do DESAFIO 028
# onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.


from  random import randint
computador = randint ( 0,10)
escolha =int(input('EM QUE NÚMERO ENTRE 0 A 10. EU ESTOU PENSANDO:'))
cont = 1
while computador != escolha:
    escolha =int(input('EM QUE NÚMERO ENTRE 0 A 10. EU ESTOU PENSANDO'))
    cont += 1
print(f'você acertou e usou {cont} paltites')



