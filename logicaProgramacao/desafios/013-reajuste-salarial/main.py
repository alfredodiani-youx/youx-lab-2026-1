s = float(input('Qual o salário do funcionário? R$'));
r = s + (s * 15 /100);
print('O funcionário que recebia R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, r));
