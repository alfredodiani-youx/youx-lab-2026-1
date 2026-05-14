reta1 = float(input('Qual é o comprimento da reta: '))
reta2 = float(input('Qual é o comprimento da reta: '))
reta3 = float(input('Qual é o comprimento da reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 + reta1 + reta3:
    print('Os segmentos podem formar um triângulo. ')
else:
    print('Os segmentos não podem formar triângulo. ')