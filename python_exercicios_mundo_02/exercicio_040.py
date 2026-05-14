#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

    #Média abaixo de 5.0: REPROVADO
    #Média entre 5.0 e 6.9: RECUPERAÇÃO
    #Média 7.0 ou superior: APROVADO


nota1 = float(input("Qual foi sua primeira nota? "))
nota2 = float(input("Qual foi sua segunda nota? "))
media = (nota1 + nota2) / 2
print("Tirando {} e {},a média do aluno é {}".format(nota1, nota2, media))
if media < 5.0:
    print("REPROVADO")
elif media == 5.0 or media < 6.9:
    print("RECUPERAÇÃO")
elif media >= 7.0:
    print("APROVADO")
