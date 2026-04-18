idm = 0
hc = 0
mm = 0
while True:
    print("-"*30)
    print("    CADASTRE UMA PESSOA")
    print("-"*30)
    id = int(input("Idade: "))
    if id > 18:
        idm += 1
    se = input("Sexo [M/F]: ").strip()[0]
    if se in "Mm":
        hc += 1
    if se in "Ff" and id < 20:
        mm += 1
    o = input("Quer cadastrar mais pessoas?: ").strip()[0]
    if o in "Nn":
        break
print("Total pessoas maiores de 18 anos: {}".format(idm))
print("Ao todo temos {} homens cadastrado".format(hc))
print("E temos {} mulheres com menos de 20 anos".format(mm))