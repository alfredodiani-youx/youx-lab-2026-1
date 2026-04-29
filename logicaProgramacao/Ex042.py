Segmento = float(input('Digite o primeiro segmento: '))
Seg2 = float(input('Digite o segundo segmento: '))
Seg3 = float(input('Digite o terceiro segmento: '))
if (Segmento + Seg2 > Seg3) and (Segmento + Seg3 > Seg2) and (Seg3 + Seg2 > Segmento):
    print(f'os segmentos {Segmento},{Seg2},e {Seg3} juntos podem formar um triangulo')
else:
    print('Os segmentos nao podem formar um triangulo')
if Segmento == Seg2 == Seg3:
    print('Os segmentos formam um triangulo equilatero')
elif Segmento == Seg2 or Segmento == Seg3 or Seg2 == Seg3:
    print('Os segmentos formam um isosceles')
elif Segmento != Seg2 or Segmento != Seg3 or Seg2 == Seg3:
    print('Os segmentos formam um escaleno')