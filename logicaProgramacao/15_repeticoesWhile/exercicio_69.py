maiorIdade= homem = mulher = 0
while True:
    idade= int(input('digite sua idade :'))
    sexo= ' '
    while sexo not in 'MF':
        sexo= str(input('qual seu sexo [M/F] :')).strip().upper()
    if idade >= 18:
        maiorIdade += 1
    if sexo == 'M':
         homem += 1
    if sexo == 'F' and idade <20:
        mulher += 1
    resposta= ' '
    while resposta not in 'SN':
        resposta= str(input('deseja continuar? [S/N]')).strip().upper()
    if resposta == 'N':
        break
print(f'temos {maiorIdade} pessoas com mais de 18')
print(f'temos no total {homem} homens')
print(f'temos {mulher} mulheres com mais de 20 anos ')

