def formatar(txt):
    texto = str(txt)
    pos_virg = texto.find(".")
    if (len(texto) - 1) - pos_virg == 0:
        texto += "00"
    elif (len(texto) - 1) - pos_virg == 1:
        texto += "0"
    texto = texto.replace(".", ",")
    return f"R${texto}"