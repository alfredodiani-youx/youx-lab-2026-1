from math import sqrt

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
print('Sua parede tem a dimensão de {}*{} e sua área é de {} metros ao quadrado'.format(largura, altura, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
