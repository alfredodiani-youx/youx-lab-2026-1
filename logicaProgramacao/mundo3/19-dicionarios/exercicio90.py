aluno= {}
aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = input(f"Digite a media: ")
print(f"Nome: {aluno['nome']} \n {aluno['media']}")
if aluno['media'] >= 7:
    print("Aprovado")
else:
    print("Recuperaçao")
