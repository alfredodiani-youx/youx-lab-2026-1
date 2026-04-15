d = float(input("Digite a disância da viagem: "));
if d < 200:
    v = 0.5;
else: 
    v = 0.45;
print("A viagem de {}Km sairá por R$ {}".format(d, d * v))