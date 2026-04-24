a = float(input('Qual a altura da parede em metros: '))
l = float(input('Qual a largura da parede em metros: '))
r = a * l
t = r / 2
print('Essa parede tem {} metros quadrados, sera necessario {} litros de tinta' .format(r , t))