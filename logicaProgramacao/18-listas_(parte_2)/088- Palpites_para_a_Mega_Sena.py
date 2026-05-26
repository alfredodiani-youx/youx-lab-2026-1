from random import sample
print('joga na mega sena')
quantidade =int(input('quantas apostas vc dejesa gerar: '))
coisa = [sample(range(1, 61), k= 6)for numero in range(0, quantidade)]
for c in range(0, quantidade):
    print(f'a aposta {c + 1}:{sorted(coisa)[c]}')