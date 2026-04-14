l = int(input('Digite a largura da parede: '));
a = int(input('Digite a altura da parede: '));
area = l * a;
print('Sua parede tem a dimensão {}x{}, e a área de {}m².'.format( l, a, area));
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta));
