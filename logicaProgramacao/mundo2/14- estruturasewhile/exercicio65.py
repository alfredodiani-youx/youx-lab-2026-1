resposta = 'S'
soma = quanto = media = maior = menor = 0
while resposta in 'Ss':
        numero =int(input('digite um número:'))
        soma += numero
        quanto += 1
        if quanto == 1:
             maior = menor = numero
        else:
             if numero > maior:
                maior = numero
             if numero < menor:
                     menor = numero
        resposta =str(input('quer continuar? [sim/não]')).upper().strip()[0]
media = soma / quanto
print(f'você digitou {quanto} números e a media foi {media}')
print(f' o maior valor foi {maior} e o menor foi {menor}')
