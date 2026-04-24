km = float(input('Quantos kilometros tem sua viagem? '))
if km <=200:
    print('O valor da passagem e R${:.2f}' .format(km * 0.50))
else:
    print('O valor da passagem e R${:.2f}' .format(km * 0.45))