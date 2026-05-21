sexo = input("Digite seu sexo [H/M]: ").strip()
while sexo not in 'MmHh':
   sexo = input("Dados invalidos! Por favor digite seu sexo: ").strip()
print("Pronto")