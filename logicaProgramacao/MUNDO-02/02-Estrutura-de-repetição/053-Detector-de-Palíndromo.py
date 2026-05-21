frase = str(input('Digite seu nome aqui \u27A1: ' )).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    print(junto[letras], end= '')