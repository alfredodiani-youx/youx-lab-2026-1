l = ""
first = ""
pa = 0
for i in range(0, 4):
    n = int(input(f"Digite o {i+1}° número: "))
    if i == 0:
        first = str(n)
    if n % 2 == 0:
        pa += 1
    l = l + f"{int(n)} "
    ls = tuple(l.split())
print(f"Você digitou os valores: {ls}")
print(f"O número {first} apareceu {ls.count(first)} vezes")
if "3" in ls:
    print(f"O número 3 apareceu na {l.split().index("3")+1}° posição")
else:
    print(f"O número 3 não apareceu em nenhuma posição")
print(f"Ao todo foram digitado {pa} números pares")
