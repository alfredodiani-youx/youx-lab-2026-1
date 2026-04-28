Carro = int(input('Qual a velocidade do carro? '))
multa = (Carro - 80)*7
if Carro < 80:
    print('Tenha um bom dia e dirija com seguranca!')
else:
    print(f"Voce foi multado em {multa}R$ por ultrapassar a velocidade de 80km/h")
