reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 + reta1 + reta3:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
    if reta1 == reta2 == reta3:
        print('Os segmentos acima PODEM FORMAR um triângulo equilátero.')
    if reta1 == reta2 != reta3:
        print('Os segmentos acima PODEM FORMAR um triângulo isósceles.')
    if reta1 != reta2 != reta3:
        print('Os segmentos acima PODEM FORMAR um triângulo escaleno.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')