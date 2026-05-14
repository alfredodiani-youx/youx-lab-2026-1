numero=None
contador = 0
soma = 0
while numero !=999:
        numero=int(input('Digite um número: '))
        contador += 1
        soma += numero
print(f'A soma entre os {contador} números é: {soma}')