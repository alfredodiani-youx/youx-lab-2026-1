# def título(txt):
#     print('-'*30)
#     print(txt)
#     print('-'*30)
# título('        CURSO EM VÍDEO   ')
# título('        APRENDA PYTHON   ')
# título('        GUSTAVO GUANABARA   ')
from hmac import digest_size


# a = 4
# b = 5
# s = a+ b
# print(s)
#
# a = 8
# b = 9
# s = a + b
# print(s)
#
# a = 2
# b = 1
# s = a + b
# print(s)



#Programa Principal
# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     print(f'A soma de A + B é igual a: ', end='')
#     s = a + b
#     print(s)
#
#
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)



# def contador(* num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e ao todo são {tam} números')
#
#
# contador(2, 7, 1)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)



def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)