n = str(input('Digite seu nome completo: '))
ns = n.split()

print('Pazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é: {}'.format(ns[0]))
print('Seu último nome é: {}'.format(ns[len(ns)-1]))
