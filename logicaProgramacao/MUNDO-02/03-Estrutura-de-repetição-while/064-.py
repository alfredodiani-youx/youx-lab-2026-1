num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input("Digite um numero: "))
    soma += num
    cont += 1
print(f"Voce digitou {cont - 1} numero e a soma de todos é {soma - 999}")