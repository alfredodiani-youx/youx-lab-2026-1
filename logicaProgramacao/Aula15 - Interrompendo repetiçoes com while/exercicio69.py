#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
cont_i = 0
cont_h = 0
cont_i20 = 0
while True:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        cont_i += 1
    sexo = input("Digite seu sexo[M/F]: ")
    if sexo in 'Mm':
        cont_h += 1
    if sexo in 'Ff' and idade < 20:
        cont_i20 += 1
    r = input("Voce deseja continuar? [S/N]").upper()
    if r == 'N':
        break
print(f"Total de pessoas com ou mais de 18 anos {cont_i} \n Total de mulheres com menos de 20 anos {cont_i20} \n TOtal de homens {cont_h}")