def m(n):
        return f"{n / 2:.2f}".replace(".", ",")

def d(n):
    return f"{n * 2:.2f}".replace(".", ",")

def pt(n):
    return f"{n * 1.35:.2f}".replace(".", ",")
def r(n):
    n = n.replace(",", ".")
    if n.replace(".", "", 1).isdigit():
        n = float(n)
        dobro = n * 2; metade = n / 2; p1 = n + (n * (35 /100)); p2 = n - (n * (22 /100))
        print("-"*25)
        print("    RESUMO DO VALOR")
        print("-"*25)
        print(f"Preço analisado: {n:.2f}".replace(".", ","))
        print(f"Metade de {n}: {metade:.2f}".replace(".", ","))
        print(f"Dobro de {n}: {dobro:.2f}".replace(".", ","))
        print(f"35% de aumento: {p1:.2f}".replace(".", ","))
        print(f"22% de redução: {p2:.2f}".replace(".", ","))

    else:
        print("Valor inválido")