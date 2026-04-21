al = {}
al["nome"] = input("nome: ")
al["media"] = float(input(f"média de {al['nome']}: "))
print("-="*20)
s = "   "
print(f"{s}- o nome do aluno é {al['nome']}")
print(f"{s}- a nota média de {al['nome']} é {al['media']:.2}")
if al['media'] <= 5:
    print(f"{s}- {al['nome']} foi reprovado!")
elif al['media'] <= 7:
    print(f"{s}- {al['nome']} está de recuperação!")
elif al['media'] > 7:
    print(f"{s}- {al['nome']} foi aprovado!")