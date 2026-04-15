f = str(input("Digite sua frase:")).upper().strip();
print("A letra A aparece na frase {} vezes".format(f.count("A")));
print("A primeira letra A apareceu na posição {}".format(f.find("A")+1));
print("A última letra A apareceu na posição {}".format(f.rfind("A")+1));