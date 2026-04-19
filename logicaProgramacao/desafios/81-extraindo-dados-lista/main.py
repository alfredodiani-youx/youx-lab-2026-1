l = []
while True:
    l.append(int(input("Digite um valor: ")))
    o = input("Deseja continuar? [S/N]: ")
    if o in "Nn":
        break
l.sort()
print(f"Você digitou {len(l)} elementos.")
print(f"Os valores em ordem crescente são: {l[::-1]}")
if 5 in l:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não está na lista.")