palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar')

for i in palavras:
    print(f'na palavra {i} temos as vogais: ',end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra,end='')
    print(f'\n {"-="*20}')