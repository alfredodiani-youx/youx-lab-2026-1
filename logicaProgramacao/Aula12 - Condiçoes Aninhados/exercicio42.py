#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes


a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print(f'os segmentos {a} , {b} e {c} podem formar um triangulo')
    if a == b and a == c:
        print("É um triangulo equilatero")
    elif a == b and a != c:
        print("É um triangulo isosceles")
    elif a != b and a != c:
        print("É um triangulo escaleno")
    else:
        print(f"Com os segmentos {a} , {b} , e {c} nao é possivel formar um triangulo ")
else:
    print(f"Com os segmentos {a} , {b} , e {c} nao é possivel formar um triangulo ")
