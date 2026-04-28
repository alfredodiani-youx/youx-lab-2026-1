palavras = ('estudar', 'aprender', 'python', 'curso', 'linguagem', 'praticar', 'trabalhar', 'programador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')