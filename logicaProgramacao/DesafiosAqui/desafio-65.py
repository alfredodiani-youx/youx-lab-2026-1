res='S'
soma = 0
contador = 0
media = None
while res =='S':
        numero=int(input('Digite um número: '))
        res=str(input('Que continuar? [S/N] ')).upper()
        contador += 1
        soma += numero
        media = (soma/contador)/1
print(f'A média entre os {contador} números é {media}')