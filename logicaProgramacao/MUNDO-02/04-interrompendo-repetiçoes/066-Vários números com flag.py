cont = 0
soma = 0
while  True:
    num = int(input("Digite um numero[ Digite 999 para parar ]: "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"Voce digitou {cont} numeros e a soma entre eles é {soma}")