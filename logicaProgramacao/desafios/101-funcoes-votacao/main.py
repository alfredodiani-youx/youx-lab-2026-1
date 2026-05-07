from datetime import datetime


def voto():
    idade = 0
    print('-'*30)
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento
    print(f'Com {idade} anos: ', end='')
    if idade > 18 and idade <= 65:
        print('VOTO OBRIGATÓRIO.')
    elif idade < 16:
        print('NÃO VOTA.')
    elif idade >= 16 and idade <18:
        print('VOTO OPCIONAL.')
    elif idade > 65:
        print('VOTO OPCIONAL.')

nascimento = int(input('Em que ano você nasceu? '))
voto()