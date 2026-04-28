num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 foi digitado {num.count(9)} vez(es)')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}º posição')
else:
    print('Não foi digitado nenhum número 3')
print(f'Os valores pares digitados foram ', end='')
for pares in num:
    if pares % 2 == 0:
        print(pares, end= ' ')