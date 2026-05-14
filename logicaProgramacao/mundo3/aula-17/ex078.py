valores = []
for i in range(5):
    valores.append(int(input(f'Digite um valor para a Posicao {i}: ')))
print(valores)
print(max(valores))
print(min(valores))
print(valores.index(max(valores)))
print(valores.index(min(valores)))
