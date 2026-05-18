palavras= ('bala',
           'mesa',
           'casa',
           'computador',
           'escola',
           'celular',
           'pessoa')
for p in palavras:
    print(f'na palavra {p.upper()} temos', end= ' ')
    for letra in p:
        if letra.lower() in 'a,e,i,o,u':
            print(letra, end= ' ')