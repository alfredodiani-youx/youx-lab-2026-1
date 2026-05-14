frase = str(input('Digite uma frase: ')).replace(' ', '')
separado = frase.strip()
junto = ''.join(separado)
inverso = ''
for letras in range(len(frase)-1, -1, -1):
    inverso += junto [letras]
    print(inverso)
if inverso == junto:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')