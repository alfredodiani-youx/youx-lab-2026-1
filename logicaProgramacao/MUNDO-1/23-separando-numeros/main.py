n1 = int(input('um valor'))
unidade = n1 // 1 % 10
dezena = n1 // 10 % 10
centena = n1 // 100 % 10
milhares = n1 // 1000 % 10
print(f" a unidades desse numero é {unidade}")
print(f"a dezena desse numero é {dezena}")
print(f"a centena desse numero é {centena}")
print(f"o milhar desse numero é {milhares}")