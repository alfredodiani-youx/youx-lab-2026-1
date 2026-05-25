def escreva(palavra):
    tam = len(palavra)+4
    print('~'*tam)
    print(palavra.center(tam))
    print('~'*tam)

escreva('HELLO WORLD')