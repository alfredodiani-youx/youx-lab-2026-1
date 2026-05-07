#CONDIÇAO

#if carro.esquerdo():
    #bloco True
#else:
  #bloco False

#Ex: tempo = int(input('Quantos anos tem seu carro?'))
#if tempo<=3:
#print('carro novo')
#else:
#print('carro velho')
#print('--FIM--')

#Ex: tempo = int(input('Quantos anos tem seu carro?))
#print('carro novo'if tempo<=3else'carro velho')
#print('--FIM--')

nome = str(input('Qual é o seu nome? '))
if nome == 'Ana Carneiro':
    print('Que nome lindo você tem!!')
else:
    print('Seu nome é tao normal!')
print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa!PARABENS!')
else:
    print('Sua media foi RUIM!ESTUDE MAIS!')