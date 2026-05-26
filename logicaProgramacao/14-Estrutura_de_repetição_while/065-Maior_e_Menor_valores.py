n =int(input('digite um numero: '))
pergunta =str(input('deseja continuar?[S/N]: ')).upper()
quantidade = 0
while pergunta!= 'n':
    numero = int(input('digite um numero: '))
    pergunta = str(input('deseja continuar?[S/N]: '))
    if pergunta == 'n':
        m = (numero + quantidade) / 2
        print(f'voce digitou {quantidade} numeros...sua media é {m}')
        print('o maior numero foi', max(n, numero))
        print('o menor numero foi', min(n, numero))
