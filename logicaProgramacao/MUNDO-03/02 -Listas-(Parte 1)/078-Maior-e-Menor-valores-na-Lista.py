lista_numero = []
maior = 0
menor = 0
opcao = ''
for numero in range(1, 5+1):
    num = int(input("Digite um valor: "))
    lista_numero.append(num)
    menor = num
    maior = num
    opcao = input("Deseja continuar[SIM/NÃO] ").upper()
    if 'N' in opcao:
        break
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(lista_numero)
print(f"O menor numero é  {menor} e o maior é {maior}")