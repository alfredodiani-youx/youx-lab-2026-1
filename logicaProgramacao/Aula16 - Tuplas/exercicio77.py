#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("APRENDER" , "PROGRAMAR" , "LINGUAGEM" , "PYTHON" , "CURSO" , "GRATIS" , "ESTUDAR" , "PRATICAR" , "TRABALHAR" , "MERCADO" , "PROGRAMADOR" , "FUTURO")
for v in palavras:
    print(f"\n NA PALAVRA {v.upper()} TEMOS" , end= ' ')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(letra, end='')