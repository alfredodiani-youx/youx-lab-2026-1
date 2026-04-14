#Crie um codigo que leia a temperatura digitada e a converta para fahrenheit

temperatura = float(input("Digite a temperatura em ºC: "))
conversor = ( temperatura * 9 / 5 ) +32
print (f"A temperatura de {temperatura}ºC corresponde a {conversor} ºF")