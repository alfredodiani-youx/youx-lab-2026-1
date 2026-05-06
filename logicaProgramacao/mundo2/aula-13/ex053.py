f = input('Digite a frase ou a palavra: ')
fl = f[::-1].lower().replace('', '');
if fl == f.replace('',''):
    print(f'A frase {f} ao contrario fica {f}, entao ela e palindromo')
else:
    print(f'A frase {f} ao contrario fica {f[::-1]}, entao ela nao e um palindromo')
