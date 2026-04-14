
dia = int(input("Alugou por quantos dias?  "))
km = float(input("Qual foi a quilometragem percorrida? "))
calculo = (dia * 60) + (km * 0.15)
print(f"O total a ser pago é R${calculo:.2f}")