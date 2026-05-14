from random import randint
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
if jogador == computador:
    print('Párabens, você venceu de mim! ')
else:  print(f"GANHEI! Eu pensei no número {(computador)} e não no {jogador}!")