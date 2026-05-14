ps=int(input('Qual seu peso? '))
al=float(input('Qual sua altura? '))
pas1=(al*al)
imc=ps/pas1
if imc<18.5:
    print('Abaixo do peso')
elif imc<25:
    print('Peso ideal')
elif imc<30:
    print('Sobrepeso')
elif imc<40:
    print('Obesidade')
elif imc>40:
    print('Obesidade mórbida')
