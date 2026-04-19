pa = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar')
for i in pa:
    print(f"Na palavra {i.upper()} temos as vogais: ", end="")
    for l in i:
        if l.lower() in "aeiou":
            print(l, end="")
    print("\n {}".format("-" * 20))