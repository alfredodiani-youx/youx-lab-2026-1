primeiro = int(input('primeiro termo:'))
razao = int(input('digite a razão:'))
contador = 1
while contador <= 10:
    if contador == 1:
        print( primeiro, end = '-> ')
    segundo = primeiro + razao
    print(segundo, end=' -> ')
    primeiro = segundo
    contador += 1
print('Fim')