from datetime import date
soma = 0
cont = 0
totmaior = 0
totmenor = 0
atual = date.today().year
for c in range(1, 8):
    num = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
idade = atual - num
if idade >= 21:
    totmaior += 1
else:
    totmenor += 1
print('ao todo tivemos o total de {} pessoas maior'.format(totmaior))
print('e tambem tivemos {} menor de idade '.format(totmenor))
