ma = int();
im = int();
mm = int();
no = "";
for i in range(0,4):
    print("--- {}° PESSOA ---".format(i+1))
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F]: ")
    im += idade / 4;
    if sexo in "Mm" and idade >= ma:
        no = nome
        ma = idade
    if sexo in "Ff" and idade < 20:
        mm = mm+1
print("A média de idade do grupo foi {} anos\nO homem mais velho é o {} com {} anos\nAo todo tiveram {} mulheres com mais de 20 anos".format(im, no, ma, mm))