aluno = {}
aluno['Nome'] = input("Digite o nome do aluno: ").capitalize().strip()
aluno['Media'] = float(input(f"Digite a media de {aluno['Nome']}: "))
print(f"NOME: {aluno['Nome']} \n MEDIA: {aluno['Media']}")
if aluno['Media'] >= 7:
    print("Aprovado")
else:
    print("Recuperaçao")