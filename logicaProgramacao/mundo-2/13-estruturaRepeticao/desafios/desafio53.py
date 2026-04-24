f = str(input('digite uma frase: '))
e = "".join(f.split()).lower()
if e == e[::-1]:
    print('E um palindromo')
else:
    print('Não e um palindromo')