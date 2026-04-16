p = int(input('Digite o primeiro valor: '));
s = int(input('Digite o segundo valor: '));
t = int(input('Digite o terceiro valor: '));
# Verificando quem é menor
menor = p
if s<p and s<t:
    menor = s
if t<p and t<s:
    menor = t
# Verificando quem é maior
maior = p
if s>p and s>t:
    maior = s
if t>p and t>s:
    maior = t
print('O menor valor digitado foi {}'.format(menor));
print('O maior valor digitado foi {}'.format(maior));