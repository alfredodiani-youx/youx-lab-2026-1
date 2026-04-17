s = input("Informe seu sexo [M/F]: ").strip()
while s[0] not in "MmFf":
    s = input("Dados invalidos!\nInforme seu sexo [M/F]: ").strip()
print("O sexo {} foi registrado com sucesso".format(s))