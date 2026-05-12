#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(palavra):
    tam = len(palavra)+4
    print('~'*tam)
    print(palavra.center(tam))
    print('~'*tam)

escreva('HELLO WORLD')