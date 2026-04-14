nome = input("Digite se nome completo: ");
print("Analisando seu nome ele...");
print("Todo em maiúscula ficaria: {}".format(nome.upper()));
print("Todo em minúscula seria: {}".format(nome.lower()));
n = nome.split()
print("Tem ao todo {} caracteres".format(len(nome)))
print("Seu primeiro nome é: {}".format(n[0]))
print("Tem ao todo {} caracteres no seu primeiro nome".format(len(n[0])))