from time import sleep as sl

def contador(inicio, fim, passo):
    if passo ==0:
        passo = 1
    if passo <0:
        passo *= -1
    print(f"Contagem do {inicio} ate {fim} de {passo} em {passo}: ")
    sl(1)
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end='')
            sl(0.3)
            print()
    elif inicio > fim:
        for c in range(inicio, fim-1, -passo):
            print(c, end='')
            sl(0.3)
            print()
contador(1, 10, 1)
contador(10, 1, 2)
print("Agora é a sua vez")
ini = int(input("Inicio: "))
fi = int(input("Fim: "))
pas = int(input("Passo: "))
contador(ini, fi, pas)