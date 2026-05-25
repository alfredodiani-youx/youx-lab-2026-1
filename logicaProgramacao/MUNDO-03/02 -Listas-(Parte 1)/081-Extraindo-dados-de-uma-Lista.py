lista_numerica = []
cont = 0
while True:
    valor = int(input("Digite um valor: "))
    if 5 in lista_numerica:
        print(f"{lista_numerica.count(5)}")
    lista_numerica.append(valor)
    cont += 1
    r = input("Quer continuar[S/N]:").upper()
    if 'N' in r:
        break
print(f"{cont}")
lista_numerica.sort(reverse=True)
print (f"{lista_numerica.count(5)}")