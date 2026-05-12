#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homem_v = 0
menor_mulher = 0
nomeHomem = ''
soma_idade = 0
for p in range (1 , 5 ):
    n = input("Digite seu nome: ").strip().capitalize()
    sexo = input("Digite sua sexualidade (H/M): ").strip()
    idade =  int(input("Digite sua idade: "))
    soma_idade += idade
    if p == 1 and sexo in 'Hh':
        homem_v = idade
        nomeHomem = n
    if sexo in 'Hh' and idade > homem_v:
        homem_v = idade
        nomeHomem = n
    if sexo in 'Mm' and idade < 20:
        menor_mulher += 1
media_idade = soma_idade / 4
print(f"A media da idade do seu grupo é {media_idade}")
print(f"Possuindo {menor_mulher} mulheres com menos de 20 anos")
print(f"O homem mais velho é {nomeHomem} com {homem_v} anos")