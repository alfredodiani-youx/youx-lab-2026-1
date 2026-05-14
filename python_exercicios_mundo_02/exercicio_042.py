#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:

    #EQUILÁTERO: todos os lados iguais
    #ISÓSCELES: dois lados iguais, um diferente
    #ESCALENO: todos os lados diferentes


primeira = float(input("Qual é o comprimento da primeira reta? "))
segunda = float(input("Qual é o comprimento da segunda reta? "))
soma = primeira + segunda
terceiro = float(input("Qual é o comprimento da terceira reta? "))
if soma > terceiro:
    print("Pode formar um triangulo")
    if primeira == segunda and segunda == terceiro:
        print("EQUILÁTERO")
    elif primeira != segunda and segunda != terceiro:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("nao pode formar triangulo")
