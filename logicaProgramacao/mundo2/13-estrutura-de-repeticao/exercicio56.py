#Exercício Python 056: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idades = 0
quantidade_pessoas = 0
quantidade_mulheres_menor20 = 0
nome_do_homem_mais_velho = ''
idade_do_homem_mais_velho = 0

for c in range(0,4):
    nome = str(input('digite seu nome:'))
    idade =int(input('digite sua idade:'))
    sexo = 'x'
    while sexo not in "MF":
        sexo =str(input('digite seu sexo [M/F]:')).strip().upper()[0]

    soma_idades += idade
    quantidade_pessoas += 1

    if sexo == 'M':
         if idade > idade_do_homem_mais_velho:
             nome_do_homem_mais_velho = nome
             idade_do_homem_mais_velho = idade
    else:
         if idade < 20:
             quantidade_mulheres_menor20 += 1

media_idade = soma_idades / quantidade_pessoas
print(f'O HOMEM MAIS VELHO SE CHAMA {nome_do_homem_mais_velho} E POSSUI {idade_do_homem_mais_velho} ANOS')
print(f"A MEDIA DE IDADE DO GRUPO: {media_idade} ANOS ")
print(f"QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS: {quantidade_mulheres_menor20}")
