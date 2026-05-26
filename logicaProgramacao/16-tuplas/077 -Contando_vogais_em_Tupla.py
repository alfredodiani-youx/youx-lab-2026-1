lista =('aprender', 'programar', 'linguagem', 'python',
        'curso', 'gratis', 'estudar', 'praticar',
        'trabalhar', 'mercado', 'programador', 'futuro')
for p in lista:
    print(f'\nna palavra {p.upper()} temos', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')