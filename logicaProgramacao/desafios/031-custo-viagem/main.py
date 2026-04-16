p = int(input('Qual é a distância da sua viagem? '));
print('Você está prestes a a começar uma viagem de {}Km.'.format(p));
if p <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(p * 0.50));
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(p * 0.45));