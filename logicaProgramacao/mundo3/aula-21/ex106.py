def ajuda(com):
    help(com)

def título(mensagem, cor):
    tamanho = len(mensagem)
    print('~-~' * tamanho)
    print(f'{mensagem}')
    print('~-~' * tamanho)

#Programa Principal

comando = ''
while True:
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM!':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!')
