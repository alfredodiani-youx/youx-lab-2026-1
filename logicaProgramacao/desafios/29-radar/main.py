v = int(input("Digite a sua velocidade: "));
if v >= 80:
    print("sua velocidade excedeu 80km você foi multado em R$ {}".format((v-79) * 7));
else: 
    print("Velocidade ok, tenha um bom dia!")