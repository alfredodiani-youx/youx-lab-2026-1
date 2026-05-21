peso = int(input('Qual é seu Peso (KG) '))
altura = float(input('qual e sua Altura (m)'))
img = peso / (altura ** 2)
print('o img dessa pessoa e de {:.1f} '.format(img))
if img <= 18:
    print('MAGREZA')
elif img <= 24:
    print('NORMAL')
elif img <= 29:
    print('SOBREPESO')
elif img <= 34:
    print('VOCE ESTA COM OBESIDADE GRAU 1')
elif img <= 39:
    print('VOCE ESTA COM OBESIDADE SEVERA CUIDADO')
