#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
nota1 = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1} e {nota2} a media do aluno é {media} .Sendo assim")
if media >= 5 and media <7:
    print("Recuperaçao")
elif media <5:
     print("Reprovado")
else:
    print("Parabens voce passou")