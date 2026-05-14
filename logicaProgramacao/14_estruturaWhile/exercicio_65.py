resposta= 'sim'
soma= quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero= int(input("digite um numero"))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta= str(input('quer continuar?[sim/nao]')).upper().strip()
media = soma / quantidade
print(f'voce digitou {quantidade} numero e a media foi {media}')
print(f'o maior numero foi {menor} e o menor foi {menor}')