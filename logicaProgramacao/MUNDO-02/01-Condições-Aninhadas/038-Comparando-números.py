nu1 = int(input('Primeiro Numero: ' ))
nu2 = int(input('Segundo Numero: ' ))
if nu1 > nu2:
    print("\033[34m=-=-=" * 20)
    print('\033[34mO PRIMEIRO NUMERO E MAIOR')
    print("=-=-=" * 20)
elif nu2 > nu1:
    print("\033[34m=-=-=" * 20)
    print('\033[34mO SEGUNDO NUMERO E MAIOR')
    print("=-=-=" * 20)
elif nu1 == nu2:
    print("\033[31m=-=-=" * 20)
    print('\033[31m                                     OS DOIS SAO IGUAIS')
    print("=-=-=" * 20)


