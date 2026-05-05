largura = float(input('Qual é a largura da sua parede? '))
altura = float(input('Qual é a altura da sua parede? '))
area = largura * altura
print('Sua parede tem a dimensão de {},e sua area é de {}'.format(largura, altura, area))
tinta = area/2
print('Para pintar sua parede,você precisara de {}l de tinta'.format(tinta))
