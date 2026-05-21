palavras = ("APRENDER" , "PROGRAMAR" , "LINGUAGEM" , "PYTHON" , "CURSO" , "GRATIS" , "ESTUDAR" , "PRATICAR" , "TRABALHAR" , "MERCADO" , "PROGRAMADOR" , "FUTURO")
for v in palavras:
    print(f"\n NA PALAVRA {v.upper()} TEMOS" , end= ' ')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(letra, end='')