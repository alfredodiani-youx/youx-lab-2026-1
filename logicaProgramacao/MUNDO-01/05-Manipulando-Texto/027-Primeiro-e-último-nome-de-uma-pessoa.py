nome = str(input('digite seu nome completo:')).strip()
VERDE = '\033[1;35;40m'
AZUL = ('\033[1;35m')
FIM = '\033[0m'
NEGRITO = '\033[1m'

print(f"{VERDE}="*40)
print(f"{NEGRITO}>>> MUITO PRAZER EM TE CONHECER! <<<")
print(f"{VERDE}="*40 + FIM)
print('seu primeiro nome e {}'.format(nome[0]))
print('seu ultimo nome e {}'.format(nome[len(nome)-1]))