n = str(input("Digite seu nome: ")).lower().strip();
p = n.split();
print("Muito prazer em te conhecer");
print("Seu primeiro nome é: {}".format(p[0]));
print("Seu último nome é: {}".format(p[len(p)-1]));