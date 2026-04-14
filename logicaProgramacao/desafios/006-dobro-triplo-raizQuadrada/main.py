n = int(input('Digite um número: '));
d = n * 2;
t = n * 3;
r = n ** (1/2);
c = n ** (1/3);
print('O dobro de {} é {}\nO triplo é {}\nA raiz quadrada é {}\nA raiz cúbica é {:.3f}'.format(n, d, t, r, c));