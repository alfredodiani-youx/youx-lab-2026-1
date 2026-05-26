somar_para_numero = quantidade = somatorio = 0
numero =int(input('digite um numero para somar [999 para parar]: '))
while numero != 999:
    somatorio = somatorio + numero
    quantidade = quantidade + 1
    numero = int(input('digite um numero para somar [999 para parar]: '))
print(f'voce somou {quantidade} algarismos...o resultado da soma desses algarismos foi {somatorio}')